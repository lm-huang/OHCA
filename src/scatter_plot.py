import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import os

def plot_call_to_patient_times(df, custom_title=None):
    urban_data = df[df['urbanicity'] == 'urban']
    rural_data = df[df['urbanicity'] == 'rural']
    suburban_data = df[df['urbanicity'] == 'suburban']
    wilderness_data = df[df['urbanicity'] == 'wilderness']

    plt.figure(figsize=(18, 12))
    plt.suptitle(custom_title if custom_title is not None else 'Response Time Analysis', fontsize=16)

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
    plt.scatter(wilderness_data['call_to_patient_time'], wilderness_data.index, color='lightcoral', alpha=0.7)
    plt.title('Response Time (PSAP to Scene) - Wilderness')
    plt.xlabel('Call to Patient Time')
    plt.ylabel('Index')

    plt.show()

def plot_call_to_destination_times(df, custom_title=None):
    urban_data = df[df['urbanicity'] == 'urban']
    rural_data = df[df['urbanicity'] == 'rural']
    suburban_data = df[df['urbanicity'] == 'suburban']
    wilderness_data = df[df['urbanicity'] == 'wilderness']

    plt.figure(figsize=(18, 12))
    plt.suptitle(custom_title if custom_title is not None else 'Response Time Analysis', fontsize=16)

    plt.subplot(2, 2, 1)
    plt.scatter(urban_data['call_to_destination_time'], urban_data.index, color='skyblue', alpha=0.7)
    plt.title('Response Time (PSAP to ICU) - Urban')
    plt.xlabel('Time')
    plt.ylabel('Index')

    plt.subplot(2, 2, 2)
    plt.scatter(rural_data['call_to_destination_time'], rural_data.index, color='lightgreen', alpha=0.7)
    plt.title('Response Time (PSAP to ICU) - Rural')
    plt.xlabel('Time')
    plt.ylabel('Index')

    plt.subplot(2, 2, 3)
    plt.scatter(suburban_data['call_to_destination_time'], suburban_data.index, color='orange', alpha=0.7)
    plt.title('Response Time (PSAP to ICU) - Suburban')
    plt.xlabel('Time')
    plt.ylabel('Index')

    plt.subplot(2, 2, 4)
    plt.scatter(wilderness_data['call_to_destination_time'], wilderness_data.index, color='lightcoral', alpha=0.7)
    plt.title('Response Time (PSAP to ICU) - Wilderness')
    plt.xlabel('Call to Patient Time')
    plt.ylabel('Index')

    plt.show()
# Example usage:
# plot_response_times(df)
