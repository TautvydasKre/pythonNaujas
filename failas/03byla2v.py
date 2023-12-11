def sukurtiDuomenuFaila():
    with open('failas/03data.txt', 'w', encoding= 'utf-8') as f:
        f.write('10 15 -25 45 65 89\n')
        f.write('15 36 41 55 47\n')

def nuskaitytiFaila():
    with open ('failas/03data.txt', 'r', encoding='utf-8') as f:
        eil1 = f.readline().split(' ')
        eil2 = f.readline().split(' ')
        eil1Int = [int(x) for x in eil1]
        eil2Int = [int (x) for x in eil2]
        print(eil1)
        print(eil2)
        print(eil1Int , eil2Int)
    return eil1Int, eil2Int

def isaugotiDuomenis(failas, duom):
    with open (failas, 'w', encoding='utf-8') as f:
        txtDuom = str(duom)
        f.write(txtDuom[1:-1])
    

sukurtiDuomenuFaila()
list1 , list2 = nuskaitytiFaila()
print(list1)
listNew = [i for i in list1 if i % 2 ==0]
print(listNew)

isaugotiDuomenis('failas/03rez.txt', listNew)