import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data/imputed-data.csv')

urban_data = df[df['urbanicity'] == 'urban']
rural_data = df[df['urbanicity'] == 'rural']
suburban_data = df[df['urbanicity'] == 'suburban']
wild_data = df[df['urbanicity'] == 'wilderness']
plt.figure(figsize=(18, 12))

plt.subplot(2, 2, 1)
plt.scatter(urban_data['call_to_patient_time'], urban_data.index, color='skyblue', alpha=0.7)
plt.title('Response Time (PSAP to Scene) - Urban')
plt.xlabel('Time')
plt.ylabel('Index')

plt.subplot(2, 2, 2)
plt.scatter(rural_data['call_to_patient_time'], rural_data.index, color='lightgreen', alpha=0.7)
plt.title('Response Time (PSAP to Scene) - Rural')
plt.xlabel('Time')
plt.ylabel('Index')

plt.subplot(2, 2, 3)
plt.scatter(suburban_data['call_to_patient_time'], suburban_data.index, color='orange', alpha=0.7)
plt.title('Response Time (PSAP to Scene) - Suburban')
plt.xlabel('Time')
plt.ylabel('Index')

plt.subplot(2, 2, 4)
plt.scatter(wild_data['call_to_patient_time'], wild_data.index, color='lightcoral', alpha=0.7)
plt.title('Response Time (PSAP to Scene) - Wilderness')
plt.xlabel('Call to Patient Time')
plt.ylabel('Index')

plt.tight_layout()
plt.show()

# filtering data
df_res1 = df[(df['call_to_patient_time'] >= 0) & (df['call_to_patient_time'] <= 100)]

df_filtered = df_res1.dropna(subset=['urbanicity', 'call_to_patient_time'])

sns.set(style="whitegrid")

plt.figure(figsize=(12, 8))
sns.boxplot(x='call_to_patient_time', y='urbanicity', data=df_filtered)

average_response_time_by_urbanicity = df_filtered.groupby('urbanicity')['call_to_patient_time'].mean()

print("average response time for all urbanicity:")
print(average_response_time_by_urbanicity)

plt.title('Boxplot of Response Time (PSAP to Scene) by Urbanicity')
plt.xlabel('Time')
plt.ylabel('Urbanicity')

plt.show()

df_res2 = df[(df['call_to_destination_time'] >= 0) & (df['call_to_destination_time'] <= 300)]

df_filtered2 = df_res2.dropna(subset=['urbanicity', 'call_to_destination_time'])

sns.set(style="whitegrid")

plt.figure(figsize=(12, 8))
sns.boxplot(x='call_to_destination_time', y='urbanicity', data=df_filtered2)

average_response_time_by_urbanicity = df_filtered2.groupby('urbanicity')['call_to_destination_time'].mean()

plt.title('Boxplot of Response Time (PSAP to Destination) by Urbanicity')
plt.xlabel('Time')
plt.ylabel('Urbanicity')

plt.show()


