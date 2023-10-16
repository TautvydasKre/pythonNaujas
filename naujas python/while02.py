#Petriukas...
kiek = int(input('Kiek Petriukas turi pazymiu?'))
kelintas = 0
suma = 0
while kiek > kelintas:
    kelintas +=1
    paz= int(input(f'Iveskite Petriuko {kelintas}-aji pazymi'))
    if 1 <= paz <10:
        suma+=paz
    else:
        print('Blogas pazymis. kartokite ivedima')
        kelintas -=1
vid = suma / kiek
print(vid)