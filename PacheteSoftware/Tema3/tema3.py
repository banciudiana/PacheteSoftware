import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('phone_data.csv')

sms_data = df[df['item'] == 'sms']

sms_by_month = sms_data.groupby('month')['duration'].sum()
print(sms_by_month)

plt.figure(figsize=(10, 7))
sms_by_month.plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
plt.title('Suma durata a SMS-uri pe luna')
plt.show()

df_usage = pd.read_csv('user_usage.csv')
df_devices = pd.read_csv('supported_devices.csv')
df_device = pd.read_csv('user_device.csv')


result = pd.merge(df_usage,
                  df_device[['use_id', 'device']],
                  on='use_id',
                  how='left')

result = pd.merge(result,
                  df_devices,
                  left_on='device',
                  right_on='Model',
                  how='left')

traffic_by_brand = result.groupby('Retail Branding')['monthly_mb'].sum()

plt.figure(figsize=(12, 8))
traffic_by_brand.plot(kind='bar')
plt.xlabel('Brand')
plt.ylabel('Trafic total (MB)')
plt.title('Trafic total per brand')
plt.show()

df = pd.read_csv('phone_data.csv')

duration_by_month = df.groupby('month')['duration'].sum()
print("Durata pentru fiecare luna:")
print(duration_by_month)

mobile_duration = df[df['network_type'] == 'mobile'].groupby('month')['duration'].sum()
print("\nDurata pentru reteaua 'mobile' pentru fiecare luna:")
print(mobile_duration)