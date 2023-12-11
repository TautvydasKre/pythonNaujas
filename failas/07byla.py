def valom():
    with open('07data.txt', 'w') as f:
        pass

def ivedimas(txt):
    sk = int(input(f'{txt} = '))
    return sk


def rasyti(txt):
    with open('07data.txt', 'a', encoding='utf-8') as f:
        f.write(f'{txt}\n')

valom()


kiek = ivedimas('Kiek skaiciu sumuosime ')
rasyti(f'Vartotojas ivede skaiciu {kiek}')


suma = 0
list1 = []
for i in range(1, kiek+1):
    sk = ivedimas(f'sk{i}')
    rasyti(f'sk{i} = {sk }')
    suma += sk
    list1.append(sk)

print(f'Suma = {suma}')
rasyti(f'Suma = {suma}')