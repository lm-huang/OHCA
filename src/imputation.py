import sqlite3
import pandas as pd
import mapper_values
import pre_data_map as mapping


path=['data/nemsis.db','data/imputed-data.csv']
# Connection
con = sqlite3.connect(path[0])

# Corrected query with placeholder
# s
# Assuming feature_values contains attributes that are string representations of your column names
constants = mapper_values.get_cardiac_arrest_constants()

# Use the constants for your SQL query
query = """
SELECT
    TRIM(p."eTimes_07") as patient_time, 
    TRIM(p."eTimes_01") as call_time,
    TRIM(p."eTimes_11") as destination_time,
    p."eArrest_07" as aed_prior_ems, 
    p."eArrest_05" as cpr_prior_ems,
    p."eArrest_01" as cpr,
    c.Urbanicity as urbanicity
FROM 
    Pub_PCRevents_CA as p
LEFT JOIN 
    ComputedElements_CA c ON c.PcrKey = p.PcrKey 
LEFT JOIN 
    FACTPCRARRESTWITNESS_CA w ON w.PcrKey = p.PcrKey
WHERE
    TRIM(c.ageinyear) != '.';
""".format(
    patient_time=constants['TIME_INFO']['PATIENT_TIME'],
    call_time=constants['TIME_INFO']['CALL_TIME'],
    destination_time=constants['TIME_INFO']['DESTINATION_TIME'],
    aed_prior_ems=constants['CARDIAC_ARREST']['AED_PRIOR_EMS'],
    cpr_prior_ems=constants['CARDIAC_ARREST']['CPR_PRIOR_TO_EMS'],
    cpr=constants['CARDIAC_ARREST']['CPR'],
)

df = pd.read_sql(query, con)

# Simplify mapping using a loop
mappings = {
    'aed_prior_ems': mapping.map_aed,
    'cpr_prior_ems': mapping.map_cpr,
    'cpr': mapping.map_cpr_before_after,
    'patient_time': mapping.map_date_time,
    'call_time': mapping.map_date_time,
    'destination_time': mapping.map_date_time,
}

for column, func in mappings.items():
    df[column] = df[column].map(func)

# Time difference calculations
df['call_to_patient_time'] = (df['patient_time'] - df['call_time']).dt.total_seconds() / 60
df['call_to_destination_time'] = (df['destination_time'] - df['call_time']).dt.total_seconds() / 60

# 对'call_to_patient_time'和'call_to_destination_time'使用均值填充
df['call_to_patient_time'] = df['call_to_patient_time'].fillna(df['call_to_patient_time'].mean())
df['call_to_destination_time'] = df['call_to_destination_time'].fillna(df['call_to_destination_time'].mean())

# 删除除'call_to_patient_time'外的其他包含缺失值的行
df_dropped = df.dropna(subset=df.columns.difference(['call_to_patient_time']))

df_dropped.to_csv(path[1])

con.close()
