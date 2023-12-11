# try:
#     sk = int(input('Ivesk skaiciu = '))
# except ValueError:
#     print('Blogai ivesti duomenis. Mums reikia sveiko skaiciaus. ')
#     sk = int(input('Ivesk skaiciu = '))


while True:
    try:
        sk = int(input('Ivesk skaiciu = '))
        break
    except ValueError:
        print('Blogai ivesti duomenis. Mums reikia sveiko skaiciaus. ')

print(f'sk = {sk}')