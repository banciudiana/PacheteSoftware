import pandas as pd
import pandas
import csv
import json
from pprint import pprint
from itertools import islice
#citire txt

#"r" read
#"a" - Append - Deschide fișierul pentru adăugare, creează fișierul dacă nu există.
#"w" - Write - Deschide fișierul pentru scriere, creează fișierul dacă nu există.
#"x" - Create - creează fișierul, apare eroare dacă fișierul există.
#"b" - Binary - Modul binar (de ex. imagine)

f = open("Data1.txt", "r")
print(f.read())

f = open("Data1.txt", "r")
print(f.read(100))

f = open("Data1.txt", "r")
print(f.readline())

f = open("Data1.txt", "r")
for x in f:
  print(x)

# Importuri - toate grupate la începutul fișierului

# Exemplu 4. Citirea unui fișier .csv, prin intermediul bibliotecii csv
# Acest exemplu demonstrează citirea completă a unui fișier CSV rând cu rând
with open('clienti_leasing.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)

# Exemplu 5. Citirea primei coloane dintr-un fișier .csv
# Acest exemplu arată cum să extragi doar prima coloană din fiecare rând
with open('clienti_leasing.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row[0])

# Exemplu 6. Citirea primelor două coloane dintr-un fișier .csv
# Acest exemplu afișează cum să extragi și să afișezi primele două coloane
with open('clienti_leasing.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row[0],row[1]) # print (row[0:2])

# Exemplu 7. Citirea primelor zece înregistrări dintr-un fișier .csv
# Acest exemplu utilizează enumerate pentru a limita citirea la primele 10 rânduri
with open('clienti_leasing.csv', 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print(row)
        if(i >= 10):
            break

# Exemplu 8. Citirea primelor zece înregistrări dintr-un fișier .csv cu islice
# Acest exemplu folosește islice pentru o limitare mai elegantă a numărului de rânduri
with open('clienti_leasing.csv') as f:
    reader = csv.reader(f)
    for row in islice(reader, 10):
        print(row)

# Exemplu 9. Citirea unui fișier și încărcarea unor coloane în liste (vectori)
# Acest exemplu demonstrează cum să stochezi coloane specifice în liste separate
id_client = []
nume_client = []
sex = []
with open('clienti_leasing.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        id_client.append(row[0])
        nume_client.append(row[1])
        sex.append(row[3])
print(id_client)
print(nume_client)
print(sex)

# Exemplu 10. Pentru mai multe fișiere identice, poate fi realizată o funcție pentru încărcarea datelor în liste
# Acest exemplu creează o funcție reutilizabilă pentru citirea datelor din fișiere CSV
def read_f(filename):
    col1 = []
    col2 = []

    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            col1.append(row[1])
            col2.append(row[2])

    return col1, col2

col1, col2 = read_f('clienti_leasing.csv')

print(col1)
print(col2)
print(len(col1))

# Exemplu 11. Citește un fișier text cu csv.reader și prelucrează înregistrările
# Acest exemplu procesează datele identificând headerul și afișând informații formatate
with open('angajati.txt') as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Numele coloanelor sunt: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} lucreaza in departmentul {row[1]}, nascut in {row[2]}.')
            line_count += 1
    print(f'Au fost procesate {line_count} linii.')

# Exemplu 12. Citește un fișier text sub formă de dicționar
# Acest exemplu folosește DictReader pentru a citi datele ca dicționare, unde cheile sunt numele coloanelor
with open('angajati.txt') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        print(row)

# Exemplu 13. Citește un fișier text sub formă de dicționar. Specificarea delimitatorului
# Acest exemplu arată diferența între DictReader și reader când se utilizează un delimiter personalizat
with open('angajati1.txt') as f:
    reader = csv.DictReader(f, delimiter =';')
    for row in reader:
        print(row)
#vs.
with open('angajati1.txt') as f:
    reader = csv.reader(f, delimiter =';')
    for row in reader:
        print(row)

# Exemplu 14. Scrierea unui fișier .csv din liste
# Acest exemplu demonstrează cum să creezi și să scrii date într-un fișier CSV
with open('angajati.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Cosmin Antonescu', 'Marketing', 'Noiembrie'])
    writer.writerow(['Eugenia Marin', 'Vanzari', 'Iulie'])
with open('angajati.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exemplu 15. Scrierea unui fișier text
# Acest exemplu arată cum să scrii direct într-un fișier text și apoi să citești conținutul
f = open('angajati2.txt','w')
f.write('Cosmin Antonescu, Marketing, Noiembrie \n')
f.write('Eugenia Marin, Vanzari, Iulie')
f = open('angajati2.txt')
for row in f:
    print(row)

# Exemplu 16. Scrierea unui fișier .csv din dicționare
# Acest exemplu demonstrează utilizarea DictWriter pentru a scrie date din dicționare în CSV
with open('angajati1.csv', mode='w') as f:
    fieldnames = ['Nume', 'Dep', 'Luna']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Nume': 'Constantinescu Andrei', 'Dep': 'Contabilitate', 'Luna': 'Aprilie'})
    writer.writerow({'Nume': 'Iliescu Emil', 'Dep': 'IT', 'Luna': 'Mai'})


# Pachetul pandas
# Pandas oferă DataFrame și Series, structuri de date pentru manipularea tabelelor și seriilor de date

# Exemplu 17. Citirea unui fișier .csv, prin intermediul bibliotecii pandas
# Acest exemplu arată modul de bază de citire a unui CSV cu pandas
df = pandas.read_csv('clienti_leasing20.csv')
print(df)

# Exemplu 18. Afișarea prin localizare cu iloc a unor coloane din setul inițial
# Acest exemplu utilizează iloc pentru a selecta coloanele 2-3 din DataFrame
df = pandas.read_csv('clienti_leasing20.csv')
print(df.iloc[:,2:4])

# Exemplu 19. Afișarea cu iloc a unor coloane și înregistrări din setul inițial
# Acest exemplu selectează atât rânduri (8-9) cât și coloane (2-3) folosind iloc
df = pandas.read_csv('clienti_leasing20.csv')
print(df.iloc[8:10,2:4])

# Exemplu 20. Afișarea cu loc a unor coloane și a unei înregistrări din setul inițial
# Acest exemplu utilizează loc pentru a selecta date folosind etichetele rândurilor și coloanelor
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[0, 'NAME_CLIENT':'SEX'])

# Exemplu 21. Afișarea cu loc a unor coloane și înregistrări din setul inițial
# Acest exemplu arată diferite modalități de a folosi loc pentru a selecta rânduri și coloane specifice
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[[0,2], 'NAME_CLIENT':'SEX'])

df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[0, ['NAME_CLIENT','SEX']])

df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[[0,3], ['NAME_CLIENT','SEX']])


# Exemplu 22. Afișarea cu iloc și loc a unor coloane și înregistrări din dataframe inițial
# Acest exemplu compară utilizarea iloc (indexare numerică) cu loc (indexare bazată pe etichete)
df = pandas.read_csv('clienti_leasing20.csv')
print(df.iloc[0:3, [1,6,5]])
print(df.loc[0:3, 'NAME_CLIENT':'SEX'])

# Exemplu 23. Modificarea venitului pentru o anumită înregistrare
# Acest exemplu arată cum să modifici valoarea unei celule specifice într-un DataFrame
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[0, 'VENIT_PER_YEAR'])
df.loc[0,'VENIT_PER_YEAR']=30000
print(df.loc[0, 'VENIT_PER_YEAR'])

# Exemplu 24. Modificarea venitului dacă acesta este mai mic decât 5000 și vârsta este mai mare decât 30.
# Crearea cu copy() a unui dataframe df1 și calcularea salariului mediu
# Acest exemplu demonstrează filtrarea condiționată și actualizarea valorilor
df = pandas.read_csv('clienti_leasing20.csv')

df1=df.copy()

df1.loc[(df1['VENIT_PER_YEAR']<5000)&(df1['AGE']>30),'VENIT_PER_YEAR']=10000

print(df1[['NAME_CLIENT','VENIT_PER_YEAR', 'AGE']])
print(df1.loc[(df1['VENIT_PER_YEAR']==10000)&(df1['AGE']>30), ['NAME_CLIENT','VENIT_PER_YEAR', 'AGE']])

print('Salariul mediu ', df1['VENIT_PER_YEAR'].mean())

df1.to_csv('clienti_leasing20mod.csv')
df1 = pandas.read_csv('clienti_leasing20mod.csv',
            header=0,
            names=['ID', 'Nume', 'Functie', 'Sex','Moneda', 'Venit', 'Data', 'Varsta'])
df1.to_csv('clienti_leasing20mod.csv')

# Exemplu 25. Afișarea clienților cu vârsta = 35 sau sex masculin
# Acest exemplu demonstrează filtrarea cu operatori logici OR
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[(df['AGE']==35)| (df['SEX']=='m'),['NAME_CLIENT','JOB','SEX','AGE']])

# Exemplu 26. Afișarea clienților care nu dețin funcția inginer
# Acest exemplu arată cum să filtrezi negativ (exclude anumite valori)
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[df['JOB'] != 'Inginer', 'NAME_CLIENT':'VENIT_PER_YEAR'])

# Exemplu 27. Afișarea clienților al căror nume se termină în a
# Acest exemplu folosește funcții string pentru a filtra pe baza modelelor de text
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[df['NAME_CLIENT'].str.endswith("a"),['NAME_CLIENT','SEX']])

# Exemplu 28. Afișarea clienților al căror nume începe cu Ha
# Acest exemplu folosește startswith pentru a filtra texte care încep cu un anumit șir
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[df['NAME_CLIENT'].str.startswith("Ha"),['NAME_CLIENT','SEX']])
# Varianta care afișează toate coloanele cu setarea opțiunii de afișare maximă
df = pandas.read_csv('clienti_leasing20.csv')
pandas.options.display.max_columns = 10
print(df.loc[df['NAME_CLIENT'].str.startswith("Ha")])

# Exemplu 29. Afișarea clienților care dețin funcțiile inginer și profesor
# Acest exemplu folosește metoda isin pentru a căuta valori într-o listă
df = pandas.read_csv('clienti_leasing20.csv')
print(df.loc[df['JOB'].isin(['Inginer', 'Profesor']),['NAME_CLIENT','SEX', 'JOB']])

# Exemplu 30. Afișarea primelor 5 înregistrări (implicit)
# Metoda head() afișează primele 5 rânduri din DataFrame în mod implicit
df = pandas.read_csv('clienti_leasing20.csv')
print(df.head())

# Exemplu 31. Afișarea ultimelor 7 înregistrări
# Metoda tail() afișează ultimele rânduri din DataFrame
df = pandas.read_csv('clienti_leasing20.csv')
print(df.tail(7))

# Exemplu 32. Preluarea unor coloane usecols și eliminarea unor înregistrări skiprows/skipfooter din setul inițial
# Acest exemplu demonstrează citirea selectivă a datelor la încărcarea CSV-ului
df = pandas.read_csv('clienti_leasing20.csv', skiprows = [6,7,9], usecols = ['NAME_CLIENT','JOB'])
print(df)

# Exemplu 33. Identificarea și modificarea tipului de dată
# Acest exemplu arată cum să verifici și să modifici tipurile de date ale coloanelor
df = pd.read_csv('clienti_leasing20.csv')
print(df.dtypes)
df = pd.read_csv('clienti_leasing20.csv', parse_dates = ['DATA'])
df.AGE = df.AGE.astype(float)
print(df.dtypes)

# Exemplu 34. Însumarea a două valori din aceeași coloană
# Acest exemplu arată cum să accesezi și să operezi cu valori specifice din DataFrame
df = pandas.read_csv('clienti_leasing20.csv', nrows=6, usecols = ['NAME_CLIENT','VENIT_PER_YEAR'])
print(df)
print(df['VENIT_PER_YEAR'][0] + df['VENIT_PER_YEAR'][5])

# Exemplu 35. Funcția describe()
# Acest exemplu afișează statistici descriptive pentru coloanele numerice și categorice
df = pd.read_csv('clienti_leasing20.csv',usecols=['NAME_CLIENT','JOB','SEX','CURRENCY','VENIT_PER_YEAR','DATA','AGE'])
print(df.describe())
print('\n*****Functia describe() pe coloana JOB*****')
print(df['JOB'].describe())
print('\n*****Functia describe() pe coloana CURRENCY*****')
print(df['CURRENCY'].describe())

# Exemplu 36. Selectare coloane în dataframe
# Acest exemplu prezintă diferite moduri de a accesa coloanele într-un DataFrame
df = pd.read_csv('clienti_leasing20.csv',usecols=['NAME_CLIENT','JOB','SEX','CURRENCY','VENIT_PER_YEAR','DATA','AGE'])
#Selectare coloana in dataframe
print(df.JOB.head())
print(df['JOB'].head())
print(df.loc[:,'JOB'].head())
print(df.iloc[:,1].head())

# Exemplu 37. Funcții sum(), mean(), median(), nunique(), max(), min()
# Acest exemplu prezintă diferite funcții de agregare pentru analizarea datelor
df = pd.read_csv('clienti_leasing20.csv',usecols=['NAME_CLIENT','JOB','SEX','CURRENCY','VENIT_PER_YEAR','DATA','AGE'])
print('Suma veniturilor ', df['VENIT_PER_YEAR'].sum(), '\nMedia veniturilor', df['VENIT_PER_YEAR'].mean())
print('Valoarea mediana ', df['VENIT_PER_YEAR'].median())
print('Valori unice ', df['VENIT_PER_YEAR'].nunique())
print('Venitul maxim ', df['VENIT_PER_YEAR'].max())
print('Venitul minim ', df['VENIT_PER_YEAR'].min())

# Exemplu 38. Înlocuiește valoarea lipsă fillna()
# Acest exemplu demonstrează cum să tratezi valorile lipsă (NaN) în date
df = pd.read_csv('clienti_leasing20.csv',usecols=['NAME_CLIENT','JOB','SEX','CURRENCY','VENIT_PER_YEAR','DATA','AGE'])
print(df['AGE'])
print(df['AGE'].fillna('valoare lipsa'))

# Înlocuirea valorilor lipsă cu media coloanei
df = pd.read_csv('clienti_leasing20.csv',usecols=['NAME_CLIENT','JOB','SEX','CURRENCY','VENIT_PER_YEAR','DATA','AGE'])
values = df['AGE'].mean()
df['AGE'] = df['AGE'].fillna(value = values)
print(df)

# Exemplu 39. Șterge coloane
# Acest exemplu arată diferite metode de a elimina coloane din DataFrame
pd.set_option("display.max_columns",10)
df = pd.read_csv('clienti_leasing20.csv')
#Sterge o coloana cu axis = 1
df = df.drop("ID_CLIENT", axis=1)
print(df)
#Sterge o coloana cu parametrul columns
df = df.drop(columns="AGE")
print(df)
#Sterge mai multe coloane
df = df.drop(["JOB", "SEX"], axis=1)
print(df)
df.to_csv('clienti_df.csv', index = False)
#Sterge o coloana, daca inplace = True, returneaza None
df.drop("VENIT_PER_YEAR", axis=1, inplace = True)
print(df)

# Exemplu 40. Șterge înregistrări
# Acest exemplu demonstrează cum să elimini rânduri din DataFrame
pd.set_option("display.max_columns",10)
df = pd.read_csv('clienti_leasing20.csv')
# Sterge liniile 3, 5, 8
df = df.drop([3,5,8], axis=0)
print(df)
# Sterge clientii care detin functia Inginer. Pentru a sterge utilizand denumirea coloanei se seteaza indexul pe coloana respectiva
df = df.set_index("JOB")
df = df.drop("Inginer", axis=0)
print(df)
# Afisez primele cinci linii cu iloc, dupa stergerea inregistrarilor
df = df.set_index("ID_CLIENT")
df = df.iloc[0:5, ]
print(df)


# Exemplu 41. Redenumire coloane
# Acest exemplu arată diferite metode pentru a redenumi coloanele unui DataFrame
pd.set_option("display.max_columns",10)
df = pd.read_csv('clienti_leasing20.csv')

df = df.rename(columns={"ID_CLIENT": "ID"})
df = df.rename(columns={"JOB": "Functia"}); print(df)

df=df.rename(
    columns={
        "AGE": "Varsta",
        "VENIT_PER_YEAR": "Venit"
    }
)
print(df)

df=df.rename(columns=str.lower)
print(df)

# 2.3 Citire fișier .json

# Exemplu 42. Import fișier json
# Acest exemplu demonstrează citirea și afișarea datelor dintr-un fișier JSON
with open('clienti_daune.json') as f:
    data = json.load(f)
pprint(data)

# Exemplu 43. Prelucrare json. Numără frecvența de apariție a cuvintelor din Dauna din fișierul json
# Acest exemplu procesează date JSON pentru a analiza frecvența cuvintelor
#deschidem fisierul clienti_daune.json
with open ('clienti_daune.json') as f:
    data=json.load(f)
#obtinem lista tuturor cuvintelor din descrierea daunelor
lista_cuvinte=[]
for dauna in data:
      lista_cuvinte=lista_cuvinte + str(str(dauna['Dauna']).lower()).split()
print(lista_cuvinte)
# numaram cuvintele si le adaugam intr-un dictionar
dictionar = {}
for cuvant in lista_cuvinte:
    if cuvant not in dictionar:
        dictionar[cuvant] = 1
    else:
        dictionar[cuvant] += 1
#formam lista cuvintelor si a frecventei de aparitie sortata descrescator
aparitie = []
for key, value in dictionar.items():
    aparitie.append((value, key))
aparitie.sort(reverse=True)
print(aparitie)


