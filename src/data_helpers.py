from sklearn.preprocessing import StandardScaler
import pandas as pd
import sqlite3
import feature_names, feature_values
import map_feature_values as mapper
import numpy as np


path = 'data/nemsis.db'

def map_cardiac_arrest_data(data: pd.DataFrame, complete=True)-> pd.DataFrame:
    data['gender'] = data['gender'].map(mapper.map_gender)
    data['aed_prior_ems'] = data['aed_prior_ems'].map(mapper.map_aed)
    data['etiology'] = data['etiology'].map(mapper.map_etiology)
    data['cpr_prior_ems'] = data['cpr_prior_ems'].map(mapper.map_cpr)
    data['cpr'] = data['cpr'].map(mapper.map_cpr_before_after)
    data['first_monitored_rythm'] = data['first_monitored_rythm'].map(mapper.map_first_monitored_rythm)
    data['witness'] = data['witness'].map(mapper.map_witness)
    data['patient_time'] = data['patient_time'].map(mapper.map_date_time)
    data['call_time'] = data['call_time'].map(mapper.map_date_time)
    data['call_to_patient_time'] = (data['patient_time'] - data['call_time']).dt.total_seconds()/60
    data['outcome'] = data['outcome'].map(mapper.map_outcome)
    data['medication'] = data['medication'].map(mapper.map_medication)

    if complete:
        return data.dropna()
    return data

def query_data(complete=True) -> pd.DataFrame:
    con = sqlite3.connect(path)
    query = f"""
    SELECT
    TRIM({feature_names.PATIENT_TIME}) as patient_time,
    TRIM({feature_names.CALL_TIME}) as call_time,
    {feature_names.GENDER} as gender,
    {feature_names.CARDIAC_ARREST_AED_PRIOR_EMS} as aed_prior_ems,
    {feature_names.CARDIAC_ARREST_CPR_PRIOR_TO_EMS} as cpr_prior_ems,
    {feature_names.CARDIAC_ARREST_CPR} as cpr,
    {feature_names.CARDIAC_ARREST_ETIOLOGY} as etiology,
    TRIM({feature_names.CARDIAC_ARREST_FIRST_MONITORED_RYTHM}) as first_monitored_rythm,
    TRIM({feature_names.CARDIAC_ARREST_WITNESS}) as witness,
    c.Urbanicity as urbanicity,
    TRIM(ageinyear) as age,
    TRIM({feature_names.MEDICATIONS}) as medication,
    {feature_names.CARDIAC_ARREST_OUTCOME} as outcome
    FROM Pub_PCRevents_CA as p
    left join ComputedElements_CA c on c.PcrKey = p.PcrKey
    left join FACTPCRARRESTWITNESS_CA w on w.PcrKey = p.PcrKey
    left join FACTPCRMEDICATION_CA m on m.PcrKey = p.PcrKey
    """

    if complete:
        query = f""" {query}"""
    df = pd.read_sql(query, con)
    return df

def get_cardiac_arrest_data(complete=True)-> pd.DataFrame:
    # query
    df = query_data(complete=complete)

    # map
    df = map_cardiac_arrest_data(df, complete=complete)
    print(df.columns)
    return df


def prepare(data: pd.DataFrame):
    X = pd.get_dummies(data[['gender', 'cpr', 'cpr_prior_ems', 'aed_prior_ems',
                             'etiology', 'first_monitored_rythm', 'witness','medication'
                             ]])
    X['age'] = data['age'].astype(int)
    X['response_time'] = data['call_to_patient_time']
    y = data['outcome'].map(map_outcome)
    return X, y


def map_outcome(outcome):
    return 0 if outcome == 'died' else 1


def filter_age(data: pd.DataFrame, end: int, start=0)-> pd.DataFrame:
    data['age'] = data['age'].astype(int)
    return data[(data['age'] > start) & (data['age'] < end)]

