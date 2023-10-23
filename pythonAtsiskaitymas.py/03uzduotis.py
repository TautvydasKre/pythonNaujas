# N = 100
# Sugeneruoja random nuo 1 iki N(100)
# Programa siulo atspeti random sugeneruota skaiciu
# ivedus spejama skaiciu (75) programa pranesa random skaicius didesnis ar mazesnis ir siulo speti dar karta ( PVZ random skaicius didesnis uz 75 spekite 3 karta)
# Ivedus didesnius skaicius uz N programa praso pakartoti ivedima ir nesumuoja prie spejimu skaiciaus 
# Vartotojui atspejus skaiciu programa pranesa koks yra random skaicius, kiek kartu buvo speta ir kiek kartu buvo klaidingai ivestas skaicius 
# baigus zaidima siuloma zaisti dar karta
import random
n = int(input('Iveskite sveikaji skaiciu... '))
sk = random.randint(0,n)
print(f'sk={sk}')
spejamasis = int(input('Atspekite mano sugeneruota skaiciu... '))
while sk < spejamasis:
    print('jusu ivestas skaicius permazas bandykite dar karta')
    if sk > spejamasis:
        print('jusu ivestas skaicius perdidelis bandykite dar karta')
    if sk == spejamasis:
        print('Jus atspejote mano skaiciu Saunuoliukas!!!!')