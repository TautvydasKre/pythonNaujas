ak = input('Iveskite asmens koda: ')

    print('Per trumpas arba per ilgas asmens kodas')
else:

    s = int(ak[0])
    yy = int(ak[1:3])
    mm = int(ak[3:5])
    dd = int(ak[5:7])
    xxxxx = int(ak[7:11])

    if s == 3 or s == 5:
        lytis = 'Vyras'
    elif s == 4 or s == 6:
        lytis = 'Moteris'
    else:
        print('Blogas pirmas skaitmuo')
        lytis = None