from enum import Enum

class CARDIAC_ARREST_OUTCOME(Enum):
    DIED_IN_FIELD = '3018003'
    DIED_IN_EMERGENCY_DEPARTMENT = '3018001'
    ONGOING_RESUSCITATION_IN_FIELD = '3018005'
    RESUSCITATION_IN_FIELD = '3018007'
    RESUSCITATION_IN_EMERGENCY_DEPARTMENT = '3018009'
    ONGOING_RESUSCITATION_BY_OTHER_EMS = '3018011'
    NOT_APPLICABLE = '7701001'

class CARDIAC_ARREST_ETIOLOGY(Enum):
    PRESUMED = "3002001"	
    DROWNING = "3002003"	
    OVERDOSE = "3002005"
    ELECTROCUTION = "3002007"
    EXSANGUANATION ="3002009"	
    OTHER = "3002011"	
    RESPIRATORY_ASPHYXIA = "3002013"
    TRAUMA = "3002015"	
    NOT_APPLICABLE = '7701001'

class CARDIAC_ARREST_WITNESS(Enum):
    NO_WITNESS = "3004001"	
    FAMIlY = "3004003"
    HEALTHCARE_PROVIDER = "3004005"
    LAY_PERSON = "3004007"	
    NOT_APPLICABLE = '7701001'

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

class CARDIAC_ARREST_FIRST_MONITORED_RYTHM(Enum):
    ASYSTOLE = "3011001"
    PEA = "3011005"
    UNKNOWN_AED_NON_SHOCKABLE = "3011007"
    UNKNOWN_AED_SHOCKABLE_RYTHM = "3011009"
    VENTRICULAR_FIB = "3011011"	
    VENTRICULAR_TACHYCARDIA_PULSELESS = "3011013"
    NOT_APPLICABLE = '7701001'

class GENDER(Enum):
    MALE = "9906003"
    FEMALE = "9906001"
    UNKNOWN = "9906005"
    NOT_APPLICABLE = '7701001'

