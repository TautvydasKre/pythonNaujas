import random

# a, z, p

zaidejas = input('Zaidejas A, Z, P? = ').upper()
komp = random.choice(['A', 'Z', 'P'])

rezultatas = ''

# Akmuo laimi prieš žirkles (akmuo bukina ar laužo žirkles)
# Žirklės laimi prieš popierių (žirklės karpo popierių)
# Popierius laimi prieš akmenį (popierius uždengią akmenį)


if(zaidejas == komp):
    rezultatas = 'Lygu'
elif( (zaidejas == 'A' and komp == 'Z') or (zaidejas == 'Z' and komp == 'P') or (zaidejas == 'P' and komp == 'A') ):
    rezultatas = 'Laimejo zaidejas'
else:
    rezultatas = 'Laimejo kompiuteris'

print(f'Rezultatas: {rezultatas}. Zaidejas: {zaidejas}, komp: {komp}') 