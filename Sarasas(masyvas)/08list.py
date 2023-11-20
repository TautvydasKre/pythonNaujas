#sukurti sarasa mamai tik teigiami pazymiai 4 ir didesni ir apskaiciuoti vidurki.
#sukurti sarasa teciui tik teigiami 6 ir didesni ir apskaiciuoja vidurki.



kiek  = int(input('Kiek Petriukas turi pazymiu? '))
p = []
i = 0
while i < kiek:
    paz = int(input(f'Įveskite {i+1}-ąjį pažymį...'))
    # if 1<=paz<=10:
    #     p.append(paz)
    #     i += 1
    # else:
    #     print(f'Pazymys {paz} neegzistuoja. Kartokite ivedima ')
    if not(1<=paz<=10):
        print(f'Pazymys {paz} neegzistuoja. Kartokite ivedima ')
        continue
    p.append(paz)
    i += 1
       
 
 
print(f'Petriuko pazymiai {p}')
 
suma = 0
for i in p:
    suma += i
vidurkis = suma / len(p)
print(f'Petriuko vidurkis {vidurkis}')