from enum import Enum

def get_cardiac_arrest_constants():
    return {
        "CARDIAC_ARREST": {
            "DATE_TIME": "eArrest_14",
            "WITNESS": "eArrest_04",
            "CPR": "eArrest_01",
            "ETIOLOGY": "eArrest_02",
            "CPR_PRIOR_TO_EMS": "eArrest_05",
            "CPR_DISCONTINUED": "eArrest_16",
            "AED_PRIOR_EMS": "eArrest_07",
            "FIRST_MONITORED_RYTHM": "eArrest_11",
            "OUTCOME": "eArrest_18",
            "SPONTANEOUS_CIRCULATION": "eArrest_12"
        },
        "PATIENT_INFO": {
            "AGE": "ePatient_15",
            "GENDER": "ePatient_13",
            "RACE": "ePatient_14",
            "URBANICITY": "urbanicity",
            "AGE_IN_YEAR": "ageinyear"
        },
        "MEDICAL_INFO": {
            "MEDICATIONS": "eMedications_03",
            "DOSE": "eMedications_05",
            "MEDICAL_HISTORY": "eHistory_17"
        },
        "TIME_INFO": {
            "CALL_TIME": "eTimes_01",
            "PATIENT_TIME": "eTimes_07",
            "DESTINATION_TIME": "eTimes_11",
            "SCENE_ARRIVAL": "eTimes_06",
            "SCENE_DEPARTURE": "eTimes_09",
            "DESTINATION_ARRIVAL": "eTimes_11"
        },
        "RESPONSE_ELEMENTS": {
            "PRIMARY_ROLE": "eResponse_07",
            "DISPATCH_DELAY": "eResponse_08",
            "RESPONSE_DELAY": "eResponse_09",
            "SCENE_DELAY": "eResponse_10",
            "TURN_AROUND_DELAY": "eResponse_11",
            "LEVEL_OF_CARE": "eResponse_15"
        },
        "OTHER_INFO": {
            "PAYMENT_METHOD": "ePayment_01"
        }
    }

class CARDIAC_ARREST_CPR_PRIOR_TO_EMS(Enum):
    YES = "9923003"
    NO = "9923001"
    NOT_APPLICABLE = '7701001'

class CARDIAC_ARREST_CPR(Enum):
    YES_PRIOR_EMS = "3001003"
    NO = "3001001"
    YES_AFTER_EMS = "3001005"
    NOT_APPLICABLE = '7701001'

class CARDIAC_ARREST_AED_PRIOR_EMS(Enum):
    NO = "3007001"	
    YES_WITHOUT_DEFIB = "3007003"	
    YES_DEFIB = "3007005"
    NOT_APPLICABLE = '7701001'


