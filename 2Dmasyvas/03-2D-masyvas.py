#Sugeneruoti atsitiktini masyvo eiluciu ir stulpeliu skaiciu is reziu nuo 5 iki 25
#Sugeneruoti dvimati masyva, issaugoti duomenis byloje [-100 iki 100]
#nuskaityti duomenis
#rez bylos susikurimas???

import random

def duomenuFailas():
    row = random.randint(5,25)
    col = random.randint(5,25)
    listSk = []
    for i in range(row*col):
        sk= random.randint(-100,100)
        listSk.append(sk)
    with open('2Dmasyvas/data.txt', 'w')as f:
        t = str(listSk)
        txt = t[1:-1]
        f.write(txt)
    return row , col

def skaitomFaila():
    row, col = duomenuFailas()
    with open('2Dmasyvas/data.txt', 'r')as f:
        listTxt = f.read().split(', ')
        listInt = [int(i) for i in listTxt]
        print(listTxt)
        p = 0
        g = col
        duMas=[]
        for i in range(row):
            duMas.append(listInt[p:g])
            p = g
            g += col
        return duMas
def rezultatas():
    duList = skaitomFaila()
    with open ('2Dmasyvas/rez.txt', 'w') as f:
        for row in duList:
            t = str(row)
            txt = t[1:-1].replace(', ', '\t')
            f.write(f'{txt}\n')
rezultatas()