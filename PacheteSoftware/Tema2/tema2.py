import pandas as pd
import csv
import json

df = pd.read_csv('clienti_leasing.csv')
new_df = df[['NAME_CLIENT', 'DEPOSIT_AMOUNT', 'PRESCORING']][
    (df['VAL_CREDITS_RON'] == 0) & (df['DEPOSIT_AMOUNT'] > 150000)
]

new_df.loc[new_df['DEPOSIT_AMOUNT'] > 500000, 'PRESCORING'] = 6

print("Rezultatul pentru cerinta 1:")
print(new_df)

with open('clienti_daune.json') as f:
    data = json.load(f)

lista_cuvinte = []
for dauna in data:
    lista_cuvinte = lista_cuvinte + str(str(dauna['Dauna']).lower()).split()

dictionar = {}
for cuvant in lista_cuvinte:
    if cuvant not in dictionar:
        dictionar[cuvant] = 1
    else:
        dictionar[cuvant] += 1

cuvinte_excluse = ["the", "and", "to", "a"]
aparitie_filtrata = []

for cuvant, frecventa in dictionar.items():
    if frecventa > 1000 and cuvant not in cuvinte_excluse:
        aparitie_filtrata.append((frecventa, cuvant))

aparitie_filtrata.sort(reverse=True)
print("\nRezultatul pentru cerinta 2:")
print("Cuvinte cu frecventa > 1000 (fara 'the', 'and', 'to', 'a'):")
for frecventa, cuvant in aparitie_filtrata:
    print(f"{cuvant}: {frecventa}")