
#Exercitiul 1

#Să se citească un număr n < 10, să se creeze o listă de numere întregi de dimensiune n
#și să se adauge elementele citite de la tastatură.
#Să se ordoneze crescător elementele listei și să se afișeze lista.
print("-----------------Exercitiul1-----------------/n")
n=int(input("Introduceti un nr n <10:"))

if n>=10 :
    print ("Nr este mai mare decat 10")
else:
    lista=[]
    for i in range(n):
        nr=int(input(f"Introduceti elmentul {i+1}:"))
        lista.append(nr)

    print("Lista nesortata ",lista)
    lista.sort() #ptr descrescatoare
    # lista.sort(reverse=True)
    print("Lista ordonata crescator ",lista)

#2. Să se creeze o lista de 5 elemente cu denumirile unor orașe.
#Să se realizeze o funcție care returnează lungimea fiecărui element (oraș) și
# să se afișeze lista ordonată descrescător, utilizând opțiunile metodei sort(),
# în funcție de această lungime.

print("-----------------Exercitiul2----------------/n")
def lungime_oras(oras):
    return len(oras)

orase=["Arad","Braila","Bacau","Paris","Constanta"]

print("Lista initiala de orase: ",orase)

orase.sort(key=lungime_oras,reverse=True)

print("Lista ordonata descrescator: ",orase)

#3
#Să se creeze o listă de liste cu denumiri de echipamente IT
# (telefon, laptop, tableta, smart_tv), prețul și cantitatea acestora.
# Calculați valoarea fiecărui echipament, adăugați-o în listă și sortați în funcție de valoare,
# utilizand functia lamda.

print("-----------------Exercitiul3-----------------/n")

lista = [['telefon', 1000,2], ['laptop', 4500, 4], ['tableta',2000,5],['tv',2500,3]]

for echipament in lista:
    val=echipament[1]*echipament[2]
    echipament.append(val)

print("Lista cu valorile adaugate ",lista)

lista.sort(key=lambda x:x[3],reverse=True)
print("Lista sortata in functie de valoare descrescator",lista)

#4. Să se creeze două liste: lista_angajati cu numele și prenumele angajaților și
# lista_clienti cu numele și prenumele clienților.

print("-----------------Exercitiul4-----------------/n")

lista_angajati=['Popescu Vasile','Ionescu Gigel', 'Pop Maria']
lista_clienti=['Ionescu Gigel', 'Costache Ioana', 'Anton Eugenia']
#Să se afișeze numele angajatului care este și client.
lista_angajati_clienti=[]

for angajat in lista_angajati:
    if angajat in lista_clienti:
        lista_angajati_clienti.append(angajat)

print("Lista de angajati si clienti ",lista_angajati_clienti)

#5 5. Să se creeze o listă de dicționare cu următoarele chei: id, nume și
# salariul pentru următorii angajați: Popescu, Ionescu, Vasilescu.
lista = [{"id":1, "nume":"Popescu", "salariul":5000}, {"id":2, "nume":"Ionescu", "salariul":4000}, {"id":3, "nume":"Vasilescu", "salariul":6000}]
#Dacă angajații au salariul mai mic decât 5000, să se majoreze salariul cu 10%.

print("-----------------Exercitiul5-----------------/n")

print("Lista de angajati inainte modificarea salariului: ",lista)
for ang in lista:
    if ang["salariul"]<5000:
        ang["salariul"]=ang["salariul"]*1.1

print("Lista de angajati dupa modificarea salariului: ",lista)


#6 6. Să se creeze o funcție și să se determine dacă numărul primit ca parametru este sau nu prim.
print("-----------------Exercitiul6-----------------/n")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n=5
print("Nr 5 este prim? ",is_prime(n))

n=80
print("Nr 80 este prim? ",is_prime(n))

def filter_primes(li1):
    return [num for num in li1 if is_prime(num)]


###7 7. Să se creeze o listă li1, formată din primele m numere naturale,
# apoi să se realizeze o funcție prin care să se creeze o listă
# li2 formată din numerele prime ale listei li1.g
# Crearea listei li1
m = int(input("Introduceți valoarea lui m: "))
li1 = list(range(m))


def filter_primes(li1):
    return [num for num in li1 if is_prime(num)]

# Crearea listei li2 cu numere prime
li2 = filter_primes(li1)

print("Lista inițială:", li1)
print("Numerele prime din listă:", li2)