#ivedamas skaicius rasti to skaiciaus skaitmenu suma...

def sumavimas(skaicius):
    suma = 0
    while skaicius > 0:
        x1 = sk % 10
        skaicius = skaicius // 10 #sk //= 10
        suma += x1
    return(suma)

sk = int(input('iveskite skaiciu...'))
s = sumavimas(sk)
print(f'skaicius{sk} skaitmenu suma = {s}')