# sk = int(input('sk = '))
# for i in range (sk):
#     print('*'*sk)
sk = int(input('Iveskite skaiciu...'))
suma = 0
while sk > 0:
    sk1 = sk % 10
    sk //= 10
    print('*' * sk1, end=(' '))
    print()