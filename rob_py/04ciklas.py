sk = int(input("Skaicius = "))
ats = 1

print(f'{sk}!', end=' = ')

for i in range(1, sk+1):
    if(i < sk):
        print(i, end=' * ')
    else:
        print(i, end=' = ')
    ats *= i

print(ats)