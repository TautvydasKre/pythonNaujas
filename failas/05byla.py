def skaitytiDuom():
    with open('failas/05data.txt', 'r', encoding='utf-8') as f:
        txt = []
        while True:
            eil = f.readline()
            if eil:
                txt.append(eil)
            else:
                break
    return txt

visiData = skaitytiDuom()
skaiciai = []
for eil in visiData:
    eilSk= [int(x) for x in eil.split(' ') if x != '\n']
    if len(eilSk) !=0:
        skaiciai.append(eilSk)
print(skaiciai)
print(skaiciai[1][0])