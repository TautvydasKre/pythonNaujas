def ivedimas():
    n = int(input('Iveskite eiluciu skaiciu:... '))
    m = int(input('Iveskite stulpeliu skaiciu:... '))
    matrix = []
    for i in range(n):
        eil = []
        for j in range(m):
            eil.append(int(input(f'Iveskite A ({i})({j}) = ')))
        matrix.append(eil)
    return matrix
def spausdinimas():
    A = ivedimas()
    for row in A:
        for element in row:
            print(element, end=' ')
        print()

spausdinimas()
    