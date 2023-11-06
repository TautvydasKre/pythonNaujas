# 2. Įvedamas bet koks skaičius. Parašykite programą, kuri tą skaičių pavaizduotu žvaigždutėmis pradedant
# vienetais.

sk = int(input('Iveskite skaiciu = '))

for i in str(sk)[::-1]:
    for x in range(int(i)):
        print('*', end='')
    print('')