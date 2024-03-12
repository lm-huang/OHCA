import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('data/imputed-data.csv')

df = df[(df['call_to_destination_time'] >= 0) & (df['call_to_destination_time'] <= 300)]

# Counting CPR and AED usage rate among all regions
cpr = df.groupby('urbanicity')['cpr_prior_ems'].value_counts().unstack()
cpr['cpr_rate'] = 100 * (cpr['YES'] / (cpr['YES'] + cpr['NO']))
aed = df.groupby('urbanicity')['aed_prior_ems'].value_counts().unstack()
aed['aed_rate'] = 100 * (aed['YES_DEFIB'] / (aed['YES_WITHOUT_DEFIB'] + aed['YES_DEFIB'] + aed['NO']))

cpr['aed_rate'] = aed['aed_rate']
region = ['Urban', 'Suburban', 'Rural', 'Wilderness']
cpr['region'] = region

melted = pd.melt(cpr, id_vars=['region'], var_name='rate', value_vars=['cpr_rate', 'aed_rate'], value_name='value')

aed_data = melted[melted['rate'] == 'aed_rate']
cpr_data = melted[melted['rate'] == 'cpr_rate']

bar_width = 0.35
fig, ax = plt.subplots()
bar1 = ax.bar(np.arange(len(aed_data['region'])), aed_data['value'], bar_width, label='AED')
bar2 = ax.bar(np.arange(len(cpr_data['region'])) + bar_width, cpr_data['value'], bar_width, label='CPR')
ax.set_xticks(np.arange(len(aed_data['region'])) + bar_width / 2)
ax.set_xticklabels(aed_data['region'])
ax.set_ylabel('Percentage: %')
ax.set_title('AED and CPR Rates Among Regions')
ax.legend()

plt.show()
