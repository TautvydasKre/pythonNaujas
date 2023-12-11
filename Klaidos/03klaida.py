# Apskaiciuoti 100/sk

import math

while True:
    try:
        sk = int(input('Ivesk skaiciu = '))
        rez = math.sqrt(100 / sk)
        break
    except ValueError as ex:
        print(f'Klaidos pranesimas {ex}. Kartokite ivedima.')
    except ZeroDivisionError:
        print('Dalyba is 0 negalima, pakartokyte ivedima. ')
    except :
        print('Ivyko nezinoma klaida')
print(f'sk = {sk}, rez = {rez}')