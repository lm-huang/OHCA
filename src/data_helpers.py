from sklearn.preprocessing import StandardScaler 
import pandas as pd
import sqlite3
import feature_names, feature_values
import map_feature_values as mapper
import numpy as np

def map_cardiac_arrest_data(data: pd.DataFrame, complete=True)-> pd.DataFrame:
    """
    Map de-identified data to real values
    """ 
    # TODO - pass feature names to map as an argument
    data['gender'] = data['gender'].map(mapper.map_gender)
    data['aed_prior_ems'] = data['aed_prior_ems'].map(mapper.map_aed)
    data['etiology'] = data['etiology'].map(mapper.map_etiology)
    data['cpr_prior_ems'] = data['cpr_prior_ems'].map(mapper.map_cpr)
    data['cpr'] = data['cpr'].map(mapper.map_cpr_before_after)
    data['first_monitored_rythm'] = data['first_monitored_rythm'].map(mapper.map_first_monitored_rythm)
    data['witness'] = data['witness'].map(mapper.map_witness)
    # data['primary_role'] = data['primary_role'].map(mapper.map_primary_role)
    # data['dispatch_delay'] = data['dispatch_delay'].map(mapper.map_dispatch_delay)
    # data['scene_delay'] = data['scene_delay'].map(mapper.map_scene_delay)
    # data['response_delay'] = data['response_delay'].map(mapper.map_response_delay)
    # data['turn_around_delay'] = data['turn_around_delay'].map(mapper.map_turn_around_delay)
    # data['level_of_care'] = data['level_of_care'].map(mapper.map_level_of_care)
    # data['payment_method'] = data['payment_method'].map(mapper.map_payment_method)
    data['patient_time'] = data['patient_time'].map(mapper.map_date_time)
    data['call_time'] = data['call_time'].map(mapper.map_date_time)
    # data['scene_departure_time'] = data['scene_departure_time'].map(mapper.map_date_time)
    # data['scene_arrival_time'] = data['scene_arrival_time'].map(mapper.map_date_time)
    # data['destination_arrival_time'] = data['destination_arrival_time'].map(mapper.map_date_time)
    data['call_to_patient_time'] = (data['patient_time'] - data['call_time']).dt.total_seconds()/60
    # data['scene_time'] = (data['scene_departure_time'] - data['scene_arrival_time']).dt.total_seconds()/60
    # data['transport_time'] = (data['destination_arrival_time'] - data['scene_departure_time']).dt.total_seconds()/60
    data['outcome'] = data['outcome'].map(mapper.map_outcome)
    data['medication'] = data['medication'].map(mapper.map_medication)

    if complete:
        return data.dropna()
    return data

def query_data(complete=True) -> pd.DataFrame:
    # Connection - could update to use a constant for the db file name
    con = sqlite3.connect('../data/nemsis.db')

    # Query
    # Features are gender, aed_prior_ems, cpr_prior_ems, response time (call to patient time), 
    # etiology, first monitored rythm, age, and witness, primary_role
    # Outcome is survival


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
    where = f"""
    WHERE
    {feature_names.PATIENT_TIME} is not null AND {feature_names.CALL_TIME} is not null
    AND {feature_names.PATIENT_TIME} != "Not Applicable" AND {feature_names.CALL_TIME} != "Not Applicable"
    AND {feature_names.GENDER} != '7701001' AND {feature_names.CARDIAC_ARREST_AED_PRIOR_EMS} != '7701001'
    AND {feature_names.CARDIAC_ARREST_CPR_PRIOR_TO_EMS} != '7701001' AND {feature_names.CARDIAC_ARREST_ETIOLOGY} != '7701001'
    AND {feature_names.CARDIAC_ARREST_CPR} != '7701001'
    AND TRIM({feature_names.CARDIAC_ARREST_FIRST_MONITORED_RYTHM}) != '7701001'
    AND {feature_names.CARDIAC_ARREST_OUTCOME} != '7701001'
    AND TRIM(ageinyear) != '7701001' AND TRIM(ageinyear) != '.' and ageinyear is not null
    AND c.Urbanicity IS NOT NULL AND trim(c.Urbanicity) != ''
    """

    if complete:
        query = f""" {query} {where}"""
    df = pd.read_sql(query, con)
    return df

def get_cardiac_arrest_data(complete=True)-> pd.DataFrame:
    # query
    df = query_data(complete=complete)

    # map
    df = map_cardiac_arrest_data(df, complete=complete)
    print(df.columns)
    return df


def prepare_data(data: pd.DataFrame, model: str):
    """
    prepare data for modeling - encode categorical features and scale numerical features
    """
    # TODO 
    # - use feature name constants
    # - pass feature names as an argument - ie categorical, numerical features
    X = pd.get_dummies(data[['gender', 'cpr', 'cpr_prior_ems', 'aed_prior_ems', 
                             'etiology', 'first_monitored_rythm', 'witness','medication'
                             ]])
    # 'primary_role',
                            #  'dispatch_delay', 'scene_delay', 'response_delay',
                            #  'level_of_care'
    X['age'] = data['age'].astype(int)
    X['response_time'] = data['call_to_patient_time']
    y = data['outcome']
    
    # normalize numerical features for logistic regression
    if model == 'logistic':
        scaler = StandardScaler().set_output(transform="pandas")
        age = scaler.fit_transform(data[['age']])
        response_time = scaler.fit_transform(data[['call_to_patient_time']])
        X['age'] = age
        X['response_time'] = response_time
            # X['transport_time'] = data['transport_time']
            # X['scene_time'] = data['scene_time']
            # y = data['outcome'].map(map_outcome)

    if model == 'xgb':
        y = data['outcome'].map(map_outcome)
    return X, y


def map_outcome(outcome):
    if outcome == 'died':
        return 0
    return 1


def filter_response_time(data: pd.DataFrame, end: int, start=0)-> pd.DataFrame:
    """
    filter response time to remove bad data and outliers, or examine a subset of the data
    """
    data = data[data['call_to_patient_time'] < end]
    data = data[data['call_to_patient_time'] > start]
    return data

def filter_transport_time(data: pd.DataFrame, end: int, start=0)-> pd.DataFrame:
    """
    filter response time to remove bad data and outliers, or examine a subset of the data
    """
    data = data[data['transport_time'] < end]
    data = data[data['transport_time'] > start]
    return data

def filter_age(data: pd.DataFrame, end: int, start=0)-> pd.DataFrame:
    """
    filter age to remove bad data or outliers, or examine a subset of the data
    """
    data['age'] = data['age'].astype(int)
    data = data[data['age'] < end]
    data = data[data['age'] > start]
    return data