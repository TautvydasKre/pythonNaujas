
#blogai____________________________________________________________________________________
# def  kalti (vinis, k):
#     for smugis in range (1, k + 1):
#         liko = vinis - smugis
#         if liko > 0:
#             print(f'Tuk! Smugis {smugis}, liko neikaltu {liko} cm')
#         else:
#             print(f'Smugis{smugis}, vinies ikalta')
#             break
# vinis = int(input('Iveskite vinies ilgi: '))
# k = int(input('Iveskite smugiu skaiciu: '))
# kalti(vinis, k)
#gerai___________________________________________________________________________________
# viniesIlgis = int(input('Kokio ilgio vinis? '))
# k =  int(input('Kiek cm vinies ikalama? '))
# for i in range(1, viniesIlgis+1):
#     viniesIlgis = viniesIlgis - k
#     if viniesIlgis > 0 :
#         print(f'"TUK!"{i}-asis smugis. Dar liko {viniesIlgis} cm neikaltos vinies')
#     else:
#         print(f'"TUK!"{i}-asis smugis. Vinis ikalta')
#         break
#tobulai_________________________________________________________________________________
import math
viniesIlgis = int(input('Kokio ilgio vinis? '))
k =  float(input('Kiek cm vinies ikalama? '))
for i in range(1, int(math.ceil(viniesIlgis/k)+1)):
    viniesIlgis = round (viniesIlgis - k,2)
    if viniesIlgis > 0 :
        print(f'"TUK!"{i}-asis smugis. Dar liko {viniesIlgis} cm neikaltos vinies')
    else:
        print(f'"TUK!"{i}-asis smugis. Vinis ikalta')
        break