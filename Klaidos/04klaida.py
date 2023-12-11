# Apskaiciuoti 100/sk

import math
veikia = True
while veikia:
    try:
        sk = int(input('Ivesk skaiciu = '))
        rez = math.sqrt(100 / sk)
        veikia = False
    except ValueError as ex:
        print(f'Klaidos pranesimas {ex}. Kartokite ivedima.')
    except ZeroDivisionError:
        print('Dalyba is 0 negalima, pakartokyte ivedima. ')
    except :
        print('Ivyko nezinoma klaida')
    else:
        print('Panasu kad viskas gerai ')
    finally:
        print('Man dzin ar viskas gerai ar blogai. as vistiek veikiu')
print(f'sk = {sk}, rez = {rez}')