# 3. Programa prašo įvesti sveiką teigiamą skaičių n (tarkim 100). Programa sugeneruoja atsitiktinį skaičių nuo
# 1 iki n. Sugeneravus atsitiktinį skaičių vartotojui siūloma atspėti kokį skaičių sugeneravo programa. Įvedus
# spėjamą skaičių (tarkim 75) programa praneša ar sugeneruotas skaičius didesnis ar mažesnis už įvestą
# skaičių ir siūlo spėti dar kartą (tarkim „Sugeneruotas skaičius didesnis už 75. Atliksite 3 spėjimą...“). Įvedus
# didesnius skaičius už n ar neigiamus skaičius programa prašo kartoti įvedimą ir jo neprisumuoja prie spėjimų
# skaičiaus. Vartotojui atspėjus skaičių - pranešimas, koks buvo sugeneruotas skaičius ir kiek spėjimų buvo
# atlikta ir kiek buvo bandymų įvesti netinkamą skaičių. Pabaigus žaidimą – siūloma sužaisti dar kartą. 

import random

n = int(input("Skaicius n = "))
rand = random.randint(1, n)
bandymu = 0
procesas = True
zaistiDar = True

print(f'Random skaicius: {rand}')

while zaistiDar:

    while procesas:
        spejimas = int(input('Spekite skaiciu = '))
        if(spejimas == rand):
            bandymu += 1
            procesas = False
        elif(spejimas < rand):
            print('mazesnis')
        else:
            print('didesnis')