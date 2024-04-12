import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import scatter_plot as sp

df = pd.read_csv('data/imputed-data.csv')

sp.plot_call_to_patient_times(df, "Response Time(PSAP to Scene) Scatterplot by Urbanicity")
sp.plot_call_to_destination_times(df, "Response Time(PSAP to Emergency) Scatterplot by Urbanicity")

# filtering data
df_res1 = df[(df['call_to_patient_time'] >= 0) & (df['call_to_patient_time'] <= 100)]
df_res2 = df[(df['call_to_destination_time'] >= 0) & (df['call_to_destination_time'] <= 300)]

sp.plot_call_to_patient_times(df_res1, "Filtered - Response Time(PSAP to Scene) Scatterplot by Urbanicity")
sp.plot_call_to_destination_times(df_res2, "Filtered - Response Time(PSAP to Emergency) Scatterplot by Urbanicity")

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

df_filtered2 = df_res2.dropna(subset=['urbanicity', 'call_to_destination_time'])

sns.set(style="whitegrid")

plt.figure(figsize=(12, 8))
sns.boxplot(x='call_to_destination_time', y='urbanicity', data=df_filtered2)

average_response_time_by_urbanicity = df_filtered2.groupby('urbanicity')['call_to_destination_time'].mean()

plt.title('Boxplot of Response Time (PSAP to Destination) by Urbanicity')
plt.xlabel('Time')
plt.ylabel('Urbanicity')

plt.show()


