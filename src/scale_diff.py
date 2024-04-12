import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data/imputed-data.csv')

df_res1 = df[(df['call_to_patient_time'] >= 0) & (df['call_to_patient_time'] <= 100)]
df_filtered = df_res1.dropna(subset=['urbanicity', 'call_to_patient_time'])

scaler = MinMaxScaler()

fields_to_scale = ['call_to_patient_time', 'call_to_destination_time']

for field in fields_to_scale:
    df_filtered[field + '_scaled'] = df_filtered.groupby('urbanicity')[field].transform(
        lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten())


plt.figure(figsize=(12, 8))
sns.boxplot(x='call_to_patient_time_scaled', y='urbanicity', data=df_filtered)
plt.title('Scaled Boxplot of Response Time (PSAP to Scene) for Cardiac Arrest by Urbanicity')
plt.xlabel('Scaled Time')
plt.ylabel('Urbanicity')
plt.show()


plt.figure(figsize=(12, 8))
sns.boxplot(x='call_to_destination_time_scaled', y='urbanicity', data=df_filtered)
plt.title('Scaled Boxplot of Response Time (PSAP to Destination) for Cardiac Arrest by Urbanicity')
plt.xlabel('Scaled Time')