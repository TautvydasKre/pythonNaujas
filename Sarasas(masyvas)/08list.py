#sukurti sarasa mamai tik teigiami pazymiai 4 ir didesni ir apskaiciuoti vidurki.
#sukurti sarasa teciui tik teigiami 6 ir didesni ir apskaiciuoja vidurki.



kiek = int(input('Kiek Petriukas turi pazymiu? '))

p=[]

kelintas = 0
suma = 0
while kiek > kelintas:
    kelintas +=1
    paz= int(input(f'Iveskite Petriuko {kelintas}-aji pazymi '))
    if 1 <= paz <=10:
        suma+=paz
    else:
        print('Blogas pazymis. kartokite ivedima ')
        kelintas -=1
    p.append(paz)
print(f'Petriuko pazymiai {p}')

suma = 0
for i in p:
    suma += i
vidurkis = suma / len(p)
print(f'Petriuko vidurki {vidurkis}')

