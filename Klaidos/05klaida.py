# Apskaiciuoti 100/sk

import math
veikia = True
while veikia:
    try:
        sk = int(input('Ivesk skaiciu = '))
        rez = math.sqrt(100 / sk)
        veikia = False
    except:
        print('Ivyko kazkokia klaida, kartokite ivedima')
    else:
        print('Panasu kad viskas gerai ')
print(f'sk = {sk}, rez = {rez}')