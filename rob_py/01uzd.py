# Suprogramuokite programinę įrangą kavos aparatui. Pradinė kavos kaina įvedama klaviatūra. Kaina
# nurodoma eurais (tarkim 2.20). Nurodžius kavos kainą, prašoma mesti monetą. Kavos aparatas priima 10,
# 20, 50 centų arba 1, 2 eurus (klaviatūra įvedamas skaičius 10 arba 20 arba 50 arba 1 arba 2) Įmetus tinkamą
# monetą (tarkim 1), parodomas pranešimas, kiek liko sumokėti (tarkim 1.20) ir prašoma mesti monetą dar.
# Įmetus tinkamą monetą (tarkim 2), kavos aparatas išveda pranešimą: Grąža (tarkim 80 centų arba tarkim
# 1.20 euro) ir palinkima „Skanios kavos“.
# Įmetus netinkamą monetą (tarkim 58 ), išvedamas pranešimas „Netinkama moneta. Meskite dar kartą“.
# Suskaičiuoti ir išvesti pabaigoje, kiek buvo bandymų įmesti „padirbtą“ monetą ir kiek kartų buvo metama
# „tikra“ moneta

pradine_kaina = float(input('Pradine kavos kaina = '))
liko_moketi = int(pradine_kaina * 100)
blogu_bandymu = 0
geru_bandymu = 0
geros_monetos = [10, 20, 50, 1, 2] # 1 = 100 centu, 2 = 200 centu

procesas = True

print(f'Kavos kaina: {pradine_kaina}')

while procesas:
    
    moneta = int(input('Imeskite moneta (10, 20, 50, 1, 2) = '))
    if(moneta in geros_monetos):
        if(moneta == 1 or moneta == 2):
            moneta *= 100
        geru_bandymu += 1
        liko_moketi -= moneta
        if(liko_moketi <= 0):
            procesas = False
        else:
            print(f'Liko moketi: {liko_moketi}')
    else:
        blogu_bandymu += 1
        print('Netinkama moneta, meskite kita!')

else:
    print('Skanios kavos!')
    if(liko_moketi < 0):
        graza = int(liko_moketi * -1)
        if(graza > 100):
            graza /= 100
        print(f'Grąža: {graza}')
print(f'Geru monetu {geru_bandymu}, blogu: {blogu_bandymu}')