# Exemplul 1: Conversia coloanei date din șir de caractere în dată calendaristică
import dateutil
import pandas as pd
df = pd.read_csv('phone_data.csv')
print(df.dtypes)
df['date'] = df['date'].apply(dateutil.parser.parse, dayfirst=True)
print(df.dtypes)

# Exemplul 2: Prelucrări statistice simple
import pandas as pd
df = pd.read_csv('phone_data.csv')
print('Numar inregistrari')
print(df['item'].count())
print('Durata maxima a unei convorbiri/transfer date')
print(df['duration'].max())
print('Numarul total de secunde la apeluri')
print(df['duration'][df['item'] == 'call'].sum())
print('Numarul de apeluri in fiecare luna')
print(df['month'].value_counts())
print('Numar de retele - elimina duplicatele')
print(df['network'].nunique())

# Exemplul 3: Statistici descriptive în funcție de tipul coloanei cu describe()
import pandas as pd
df = pd.read_csv('phone_data.csv')
print('Statistici descriptive')
print(df['network_type'].describe())
print(df['duration'].describe())

# Exemplul 4: Posibilități grupare
import pandas as pd
df = pd.read_csv('phone_data.csv')
print(df.groupby(['item']).groups.keys())
print(len(df.groupby(['item']).groups['call']))

import pandas as pd
df = pd.read_csv('phone_data.csv')
print(df.groupby(['month']).groups.keys())
print(len(df.groupby(['month']).groups['2014-11']))

# Exemplul 5: Funcțiile max(), min(), mean(), first(), last() pot fi utilizate cu GroupBy
import pandas as pd
df = pd.read_csv('phone_data.csv')
print('Prima inregistrare din coloana item pe valori distincte')
print(df.groupby('item').first())
print('Durata insumata pentru fiecare luna')
print(df.groupby('month')['duration'].sum())
print('Durata insumata pe convorbiri (calls), pentru fiecare retea')
print(df[df['item'] == 'call'].groupby('network')['duration'].sum())

# Exemplul 6: Grupări complexe
import pandas as pd
df = pd.read_csv('phone_data.csv')
print('Numarul de apeluri, sms, transfer date pentru fiecare luna')
print(df.groupby(['month', 'item'])['date'].count())

# Exemplul 7: Gruparea și agregarea datelor
import pandas as pd
df = pd.read_csv('phone_data.csv')
# Grupeaza dupa month si item si calculeaza statistici pentru fiecare grup
print(df.groupby(['month', 'item']).agg({'duration':sum,      # calculeaza suma duratelor dupa fiecare grup
                                     'network_type': "count", # numarul de tipuri de retele
                                     'date': 'first'}))    # arata prima aparitie (data) pentru fiecare grup
df1 = df.groupby(['month', 'item']).agg({'duration':sum,      # calculeaza suma duratelor dupa fiecare grup
                                     'network_type': "count", # numarul de tipuri de retele
                                     'date': 'first'})
df1.to_csv('agregare.csv')

# Exemplul 8: Aplicarea unor funcții multiple unei singure coloane din grup
import pandas as pd
df = pd.read_csv('phone_data.csv')
# Grupeaza dupa month si item. Calculeaza statistici pentru fiecare grup
print(df.groupby(['month', 'item']).agg({'duration': [min, max, sum],      # calculeaza min, max, si sum pentru duration
                                     'network_type': "count", # calculeaza numarul de network_type
                                     'date': [min, 'first', 'nunique']}))    # calculeaza min, first, si numarul de date unice per grup

# Exemplul 9: Inner merge sau inner join
import pandas as pd
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())

# Exemplul 10: Left merge sau left join
import pandas as pd
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='left')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())

# Exemplul 11: Right merge sau right join
import pandas as pd
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='right')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())

# Exemplul 12: Full outer merge sau full outer join
import pandas as pd
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='outer')
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())

# Exemplul 13: Full outer merge sau full outer join cu indicația _merge
import pandas as pd
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='outer',
                  indicator=True)
print(result)
print('Structura fisier user_usage.csv ', df.shape)
print('Structura fisier user_device.csv ', df1.shape)
print(df['use_id'].isin(df1['use_id']).value_counts())

# Exemplul 14: Merge utilizând trei seturi de date
import pandas as pd
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')
df3 = pd.read_csv('supported_devices.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='left')

df3.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
result = pd.merge(result,
                  df3[['manufacturer', 'Model']],
                  left_on='device',
                  right_on='Model',
                  how='left')
print(result.head())
print(result.shape)

# Exemplul 15: Groupby și agg utilizând setul rezultat
import pandas as pd
df = pd.read_csv('user_usage.csv')
df1 = pd.read_csv('user_device.csv')
df3 = pd.read_csv('supported_devices.csv')

result = pd.merge(df,
                  df1[['use_id', 'platform', 'device']],
                  on='use_id',
                  how='left')

df3.rename(columns={"Retail Branding": "manufacturer"}, inplace=True)
result = pd.merge(result,
                  df3[['manufacturer', 'Model']],
                  left_on='device',
                  right_on='Model',
                  how='left')
print(result.groupby("manufacturer").agg({
    "outgoing_mins_per_month": "mean",
    "outgoing_sms_per_month": "mean",
    "monthly_mb": "mean",
    "use_id": "count"
}))

# Exemplul 16: Reprezentare grafică cu bare cu matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", 10)
df = pd.read_csv('clienti_leasing20.csv')
print(df['AGE'])
df['AGE'].plot(kind='bar')
plt.xlabel('ID_CLIENT')
plt.ylabel('AGE')
plt.show()

# Exemplul 17: Histogramă cu matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", 10)
df = pd.read_csv('clienti_leasing20.csv')
print(df['AGE'])
df['AGE'].plot(kind='hist')
plt.xlabel('AGE')
plt.show()

# Exemplul 18: Grafic cu gruparea și sortarea datelor cu matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('clienti_leasing20.csv')
plot_data = df[df['SEX'] == 'm']
plot_data = plot_data.groupby('JOB')['VENIT_PER_YEAR'].sum()
plot_data.sort_values().plot(kind='bar')
plt.show()