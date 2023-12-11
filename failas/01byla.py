# r
# a
# w
# f = open ('failas/01data.txt', 'w', encoding='utf-8')
# f.write('Pirmas kartas su failu \n')
# f.write('ĄČĘĖĮŠŲŪ \n')
# a = [5,8,9,7,9]
# f.write(a)
# f.write(str(a))
# x = 5 
# y = 8
# f.write(f'\n{x} + {y} = {x+y}\n')
# f.close

# try:
#     f = open ('failas/01data.txt', 'w', encoding='utf-8')
#     f.write('Pirmas kartas su failu \n')
#     f.write('ĄČĘĖĮŠŲŪ \n')
#     a = [5,8,9,7,9]
#     f.write(a)
#     f.write(str(a))
#     x = 5 
#     y = 8
#     f.write(f'\n{x} + {y} = {x+y}\n')
# finally:
#     f.close()


with open ('failas/02data.txt', 'w', encoding='utf-8') as f:
    f.write('Pirmas kartas su failu \n')
    f.write('ĄČĘĖĮŠŲŪ \n')
    a = [5,8,9,7,9]
    f.write(a) #klaida
    f.write(str(a))
    x = 5 
    y = 8
    f.write(f'\n{x} + {y} = {x+y}\n')