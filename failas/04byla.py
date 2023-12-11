def  sukurtBylas(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)
def nuskaitytiDuomenis():
    with open(failas,'r',encoding='utf-8') as f:
        eil = f.readline()
    return eil
for i in range(1,21):
    sukurtBylas(f'failas/{i}byla.txt', f'{i} byloje irasyta informacija\n')
    print(nuskaitytiDuomenis(f'{i}byla.txt'))


# def kuriam(failas, tekstas):
#     with open(failas,'w',encoding='utf-8') as f:
#         f.write(tekstas)
# def skaitom(failas):
#     with open(failas,'r',encoding='utf-8') as f:
#         txt = f.read()
#     return txt
        
# for i in range(1, 6):
#     kuriam(f'{​​​​​​i}​​​​​​data.txt', f'{​​​​​​i}​​​​​​ byloja irasyta informacija')
#     print(skaitom(f'{​​​​​​i}​​​​​​data.txt'))