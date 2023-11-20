#Petriuko, Antano, Stasio.... pazymiai
# Ivedamas pazymiu kiekis ir suvedami pazymiai. rasti vidurki
#sukurti sarasa mamai (tik teigiami) 4 ir didesi ir apskaiciuoti vidurki
#sukurti sarasa teciui (tik teigiami) 6 ir didesi ir apskaiciuoti vidurki
MAMA = 6
TATA = 4
# -----------------FUNKCIJA GRAZINANTI PAZYMIU KIEKI ---------------------
def kiekis(vardas):
    kiek  = int(input(f'Kiek {vardas} turi pazymiu? '))
    return kiek
# ------------------------------------------------------------------------
# ---------------- FUNKCIJA PAZYMIAMS IVESTI IR GRAZINTI -----------------
def ivedimas(kiek, vardas):
    p = []
    i = 0
    while i < kiek:
        paz = int(input(f'Įveskite {vardas} {i+1}-ąjį pažymį...'))
        if 1<=paz<=10:
            p.append(paz)
            i += 1
        else:
            print(f'Pazymys {paz} neegzistuoja. Kartokite ivedima ')
    return p
# ------------------------------------------------------------------------
# ----------------FUNKCIJA APSKAICIUOJA IR GRAZINA VIDURKI ---------------
def vidurkis(p):
    if len(p) > 0:
          return (sum(p) / len(p))
    else:
        return 0
   
# ------------------------------------------------------------------------
# ------------------------ SARASAS TEVAMS --------------------------------
def tevams(p,kriterijus):
    pTev = []
    for i in p:
        if i >= kriterijus:
            pTev.append(i)
    return pTev
# ------------------------------------------------------------------------
# ------------------------ DUOMENU ISVEDIMAS -----------------------------
def isvedimas(vardas):
    # paz = ivedimas(kiekis(vardas), vardas)
    # vidMok = vidurkis(paz)
    # pazMama = tevams(paz, MAMA)
    # pazTetis = tevams(paz, TATA)
    # vidMama = vidurkis(pazMama)
    # vidTetis = vidurkis(pazTetis)
    # print(f'{vardas} pazymiai: {paz}. Vidurkis: {vidMok}')
    # print(f'{vardas} mamai pazymiai: {pazMama}. Vidurkis: {vidMama}')
    # print(f'{vardas} teciui pazymiai: {pazTetis}. Vidurkis: {vidTetis}')
 
    paz = ivedimas(kiekis(vardas), vardas)
    pazMama = tevams(paz, MAMA)
    pazTetis = tevams(paz, TATA)
    print(f'{vardas} pazymiai: {paz}. Vidurkis: {vidurkis(paz)}')
    print(f'{vardas} mamai pazymiai: {pazMama}. Vidurkis: {vidurkis(pazMama)}')
    print(f'{vardas} teciui pazymiai: {pazTetis}. Vidurkis: {vidurkis(pazTetis)}')
# ------------------------------------------------------------------------
klase = ['Petras', 'Antanas', 'Stasys', 'Rimas', 'Jonas', 'Giedrius']
for i in klase:
    isvedimas(i)
 
# kiekP = kiekis("Petras")
# pazPet = ivedimas(kiekP, "Petras")
# vidPet = vidurkis(pazPet)
# pazMamPet = tevams(pazPet, MAMA)
# pazTevPet = tevams(pazPet, TATA)
# vidMamPet = vidurkis(pazMamPet)
# vidTevPet = vidurkis(pazTevPet)
# print(vidMamPet, pazMamPet)
# print(vidTevPet, pazTevPet)
 
 
# kiekS = kiekis("Stasys")
# pazSta = ivedimas(kiekS, "Stasys")
# kiekA = kiekis("Antanas")
# pazAnt = ivedimas(kiekA, "Antanas")
 
# p = []
# i = 0
# while i < kiek:
#     paz = int(input(f'Įveskite {i+1}-ąjį pažymį...'))
#     # if 1<=paz<=10:
#     #     p.append(paz)
#     #     i += 1
#     # else:
#     #     print(f'Pazymys {paz} neegzistuoja. Kartokite ivedima ')
#     if not(1<=paz<=10):
#         print(f'Pazymys {paz} neegzistuoja. Kartokite ivedima ')
#         continue
#     p.append(paz)
#     i += 1
       
 
 
# print(f'Petriuko pazymiai {p}')
 
# suma = 0
# for i in p:
#     suma += i
# vidurkis = suma / len(p)
# print(f'Petriuko vidurkis {vidurkis}')