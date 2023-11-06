ak = int(input'Iveskite asmens koda ')
if (10000000000<=ak<99999999999):
    print('Per trumpas arba per ilgas asmens kodas')
else:
    x1 = ak // 10000000000
    x2 = ak // 1000000000 % 10
    if x1 == 3 or x1 == 5:
        Lytis = 'Vyras'
    elif x1 == 4 or x1 ==6:
        Lytis = 'Moteris'
    else:
        print('Blogas primas skaitmuo')
    print(Lytis)


