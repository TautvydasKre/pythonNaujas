# N = 100
# Sugeneruoja random nuo 1 iki N(100)
# Programa siulo atspeti random sugeneruota skaiciu
# ivedus spejama skaiciu (75) programa pranesa random skaicius didesnis ar mazesnis ir siulo speti dar karta ( PVZ random skaicius didesnis uz 75 spekite 3 karta)
# Ivedus didesnius skaicius uz N programa praso pakartoti ivedima ir nesumuoja prie spejimu skaiciaus 
# Vartotojui atspejus skaiciu programa pranesa koks yra random skaicius, kiek kartu buvo speta ir kiek kartu buvo klaidingai ivestas skaicius 
# baigus zaidima siuloma zaisti dar karta
import random

def zaidimas():
    n = int(input('Iveskite maksimalu skaiciu n:... '))
    if n <= 0:
      print('Ivestas netinkamas skaicius, iveskite nauja:...')
      return
    sk = random.randint(1, n)
    spejimai = 0

    while True:
        spejimas = int(input(f'Atspekite mano skaiciu nuo 1 iki {n}:... '))
        spejimai += 1
        if spejimas < 1 or spejimas > n: print(f'Spejimas turi būti nuo 1 iki {n}.')
        elif spejimas < sk: print(f'mano skaicius didesnis uz {spejimas}.')
        elif spejimas > sk: print(f'mano skaicius mazesnis uz {spejimas}.')
        else:
            print(f'Sveikiname! Atspejot skaiciu {sk} per {spejimai} spejimus.')
            break

    kartot = input('Ar norite zaisti dar karta? (t/n): ')
    if kartot == 't': zaidimas()
    else: print('Aciu, kad zaidet!')

zaidimas()