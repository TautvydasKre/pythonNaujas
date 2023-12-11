# w, r, a ,w+, a+
# byloje norime irasyti 3 skaicius , nuskaityti ir susumuoti ir pabaigoje irasyti


def viskas(txt):
    with open('09data.txt', 'r+')as f:
        f.write('5\n')
        f.write('15\n')
        f.write('20\n')
        f.seek(0)
        sk1 = int(f.readline())
        sk2 = int(f.readline())
        sk3 = int(f.readline())
        s = sk1 + sk2 + sk3
        f.write(txt + '\n')
        f.write(f'{sk1} + {sk2} + {sk3} = {s}\n')
for i in range(1, 6):
    viskas('Rezultatas Nr.{i}')