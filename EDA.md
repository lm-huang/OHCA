# Background

The objective of this project is to investigate the disparities in emergency care for cardiac arrest victims between rural and urban settings. 

CPR (Cardiopulmonary Resuscitation) and AED (Automated External Defibrillator) should be applied immediately when cardiac arrest (CA) occurs, typically recommended within 4 minutes, as emergency medical services (EMS) often cannot arrive within this time frame (as confirmed by the following exploratory data analysis). Therefore, timely application of CPR and AED before the arrival of an ambulance is crucial. For cardiac arrests caused by conditions such as coronary heart disease or myocardial infarction, it is generally recommended to initiate thrombolysis or surgical intervention within 2 hours. EMS response time, including the time from Public Safety Answering Point (PSAP) receipt of the emergency call to paramedics arriving at the scene, as well as the time from PSAP receipt of the emergency call to the patient's arrival at the hospital, is also of significant importance as a metric.

Given this, we specifically examined the usage of AED and CPR, as well as the response time of emergency services and the time it takes for patients to reach the hospital emergency department, with a focus on distinguishing and comparing the differences in emergency medical services between urban and rural areas.



# Initial EDA

### Make commands

```makefile
make preprocess imputation resopnse-time AEDPCR
```
### Missing data 

It is noted that there is some data missing in certain areas. We performed mean imputation for response time and removed rows with missing values for the use of AED and CPR.

<img src="/Users/huangliming/PycharmProjects/911Project/figs/missing/aed_prior_ems-bar.png" alt="aed_prior_ems-bar" style="zoom:72%;" />

<img src="/Users/huangliming/PycharmProjects/911Project/figs/missing/cpr_prior_ems-bar.png" alt="cpr_prior_ems-bar" style="zoom:72%;" />

### Response time for CA by urbanicity

The time elapsed from the reception of emergency signals by the PSAP to the arrival of rescue personnel at the scene is being statistically analyzed. It has been observed that there are some unreasonable values (negative or extremely large values). To address this issue, data filtering is being conducted, with a focus on selecting values within the range of 0 to 100 minutes. The data for the duration from PSAP to the arrival of the hospital follows the same data filtering as well, except that the range is from 0 to 300 minutes.

<img src="/Users/huangliming/PycharmProjects/911Project/figs/response_time_scatter.png" alt="response_time_scatter" style="zoom:50%;" />

Drawing two box plots, we observe that the closer to the urban area, the shorter the window period for patients to receive medical treatment. This is more favorable for patients with CA in urban areas.

<img src="/Users/huangliming/PycharmProjects/911Project/figs/res_time_PSAP-to-scene.png" alt="res_time_PSAP-to-scene" style="zoom:72%;" />

<img src="/Users/huangliming/PycharmProjects/911Project/figs/res_time_PSAP-to-des.png" alt="res_time_PSAP-to-des" style="zoom:72%;" />



![prior_usage](/Users/huangliming/PycharmProjects/911Project/figs/prior_usage.png)

The usage rates of AED and CPR before EMS arrival show little difference between urban and rural areas.
