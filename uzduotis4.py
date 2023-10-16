savDiena = int(input('Kokia savaites diena prasideda menuo? '))
a = int(input('kokia saraso pradzia '))
b = int(input('kokia saraso pabaiga '))
for i in range (1, 32):
    if a<=i<=b:
        print(f'{i}-oji menesio diena bus {savDiena} savaites diena')
    if savDiena == 7:
        savDiena = 1
    else:
        savDiena += 1
    if i== b:
        break