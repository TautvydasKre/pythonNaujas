pasirinkimas = True
while pasirinkimas:
    print('Labas ')
    atsakymas = input('Ar norite dar karta pasisveikinti? (T/N) ')
    if not (atsakymas == 'T' or atsakymas == 't'):
        pasirinkimas = False
        print('Viso gero...')