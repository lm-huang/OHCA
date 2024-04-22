import feature_values
import pandas as pd

def map_gender(gender):
    gender = str(gender)
    for enum in feature_values.GENDER:
        if gender == '7701001':
            return None
        if enum.value == gender:
            return enum.name

def map_outcome(outcome):
    outcome = str(outcome)
    if outcome in [feature_values.CARDIAC_ARREST_OUTCOME.DIED_IN_EMERGENCY_DEPARTMENT.value, feature_values.CARDIAC_ARREST_OUTCOME.DIED_IN_FIELD.value]:
        return 'died'
    return 'survived'

def map_aed(aed):
    aed = str(aed)
    for enum in feature_values.CARDIAC_ARREST_AED_PRIOR_EMS:
        if aed == '7701001':
            return None
        if enum.value == aed:
            return enum.name

def map_cpr(cpr):
    cpr = str(cpr)
    for enum in feature_values.CARDIAC_ARREST_CPR_PRIOR_TO_EMS:
        if cpr == '7701001':
            return None
        if enum.value == cpr:
            return enum.name

def map_cpr_before_after(cpr):
    cpr = str(cpr)
    for enum in feature_values.CARDIAC_ARREST_CPR:
        if cpr == '7701001':
            return None
        if enum.value == cpr:
            return enum.name

def map_etiology(etiology):
    etiology = str(etiology)
    for enum in feature_values.CARDIAC_ARREST_ETIOLOGY:
        if etiology == '7701001':
            return None
        if enum.value == etiology:
            return enum.name
    
def map_first_monitored_rythm(rythm):
    rythm = str(rythm)
    for enum in feature_values.CARDIAC_ARREST_FIRST_MONITORED_RYTHM:
        if rythm == '7701001':
            return None
        if enum.value == rythm:
            return enum.name

def map_witness(witness):
    witness = str(witness)
    for enum in feature_values.CARDIAC_ARREST_WITNESS:
        if witness == '7701001':
            return None
        if enum.value == witness:
            return enum.name

def map_date_time(date_time: str):
    try: 
        format = "%d%b%Y:%H:%M:%S"
        return pd.to_datetime(date_time, format=format)
    except:
        return None

def map_medication(medication):
    medication = str(medication).lower()
    urgent_medications_list = [
        'epinephrine', 'atropine', 'amiodarone',
        'lidocaine', 'magnesium', 'sodium bicarbonate', 'calcium'
    ]
    non_urgent_medications_list = ['saline']
    if medication in urgent_medications_list:
        return 'urgent_medications_applied'
    elif medication in non_urgent_medications_list:
        return 'normal saline'
    else:
        return 'nothing'

def map_ecg(ecg_value):
    ecg_str = str(ecg_value).lower()
    list = ['7701001', '7701003']
    if ecg_str in list:
        return 'no_heart_rate'
    else:
        return 'heart_rate'

def map_heart_rates(heart_rates):
    heart_rates = str(heart_rates).lower()
    if heart_rates in ['7701001', '7701003']:
        return 'n/a'
    elif heart_rates == '0':
        return 'no_heart_rate'
    else:
        return 'heart_rate'

def map_disposition(disposition):
    disposition = str(disposition).lower()
    if disposition in ['4212013', '4212017','4212023','4212031','4212033','4212035','4212037']:
        return 'transport'
    else:
        return 'no_transport'

def map_destinations(destinations):
    destinations = str(destinations).lower()
    if destinations in ['7701001', '7701003']:
        return 'no_transport'
    else:
        return 'transport'