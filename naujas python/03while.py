#labai mandagi programa, kuri visada sako labas
pasirinkimas = True
while pasirinkimas:
    print('Labas ')
    atsakymas = input('Ar norite dar karta pasisveikinti? (T/N) ')
    if atsakymas == 'T' or atsakymas == 't':
        continue
    else:
        pasirinkimas = False
        print('Viso gero...')
    # ifnot(atsakymas 'T' or atsakymas == 't'):
    # else:
    #     pasirinkimas = False
    #     print('Viso gero...')