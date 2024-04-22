# 911
* Stakeholders
  * [Teresa May, DO](https://www.mainehealth.org/providers/teresa-l-may-do) -- Internal Medicine, Critical Care, Pulmonary Disease, Neurocritical Care, Maine Health
  * [Christine Lary, PhD](https://roux.northeastern.edu/people/christine-lary/) -- Research Associate Professor, The Roux Institute
  * [Qingchu Jin, PhD](https://roux.northeastern.edu/people/qingchu-jin/) -- Research Scientist (Primary POC), The Roux Institute
* Story
  * The National Emergency Medical Services Information System ([NEMSIS](https://nemsis.org/)) collects, stores and shares EMS data from across the U.S.
  The NEMSIS dataset will help many organizations assess EMS needs and performance, and support better strategic planning for the EMS systems of tomorrow. 
  Data also helps benchmark performance, determine the effectiveness of clinical interventions, and facilitate cost-benefit analyses.
  The goal in this project is to help Dr. May -- a critical care physician at Maine Health -- 
  investigate strategies for improving outcomes when cardiac-arrest victims receive care from first responders.
  For example, there's evidence of disparities in rural and urban scenarios. It's unclear if this is happening in Maine.
  * The NEMSIS dataset is complex and new, so work needs to be done to
  understand and interpret the data before it can be used in a modeling study.
  Some well known facts need to be established first with the dataset.
  For example, in real world settings 90% of patients receiving care
  should receive epinephrine. 
  But previous analyses with the NEMSIS dataset suggest that only 20% of patients receive it.
  The reason for the disparity remains unclear.
  Some of the features collected in the data may provide clues. For example, there is one field in the data called "eDisposition" that
  indicates that a patient is being transported for followup care. 
  For patients that die on the scene or en route, 
  the "eDisposition" field should be missing.
  Likewise, patients that have passed will not receive epinephrine.
  Therefore, the "eDisposition" field should enter somehow into the analysis and interpretation of results, possibly in an early
  data cleaning phase.
  This kind of exploratory analysis of the NEMSIS dataset is one possible focus for the project.



# EDA

EDA results are shown in [EDA](EDA.md)



## Instructions

The objective of the EDA is to investigate the disparities in emergency care for cardiac arrest victims between rural and urban settings. Given this, we specifically examined the usage of AED and CPR, as well as the response time of emergency services and the time it takes for patients to reach the hospital emergency department, with a focus on distinguishing and comparing the differences in emergency medical services between urban and rural areas.

Using the XGBoost algorithm, our study evaluates the efficacy of emergency interventions in Out-of-Hospital Cardiac Arrest (OHCA) cases. By analyzing a wide range of clinical and contextual factors, we aim to pinpoint crucial predictors of survival. To increase prediction accuracy, we exclude cases with lengthy response times, advanced age, and logical discrepancies from our data set. This approach is intended to produce practical insights that could enhance emergency responses and increase survival rates in OHCA situations.

The [Results](results.md) contains the outcome.



## Motivations

Following our initial exploratory data analysis, we observed that while there were differences in survival rates across urban, rural, suburban, and wilderness settings, these differences exist yet are not as prominent as we expected before.

We chose to adopt a more holistic approach to evaluating OHCA survival rates, concentrating on the entire chain of survival. This comprehensive perspective allows us to better understand and improve the critical factors influencing survival outcomes.

