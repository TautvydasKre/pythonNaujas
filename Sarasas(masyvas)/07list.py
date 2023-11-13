    #Petriuko pazymiai
#ivedamas pazymiu kiekis ir suvedami pazymiai. rasti vidurki.

kiek = int(input('Kiek Petriukas turi pazymiu? '))
p=[]

kelintas = 0
suma = 0
while kiek > kelintas:
    kelintas +=1
    paz= int(input(f'Iveskite Petriuko {kelintas}-aji pazymi '))
    if 1 <= paz <=10:
        suma+=paz
        p.append(paz)
    else:
        print('Blogas pazymis. kartokite ivedima ')
        kelintas -=1
print(f'Petriuko pazymiai {p}')

for i in p:
    suma += i
vidurkis = suma / len(p)
print(f'Petriuko vidurki {vidurkis}')

