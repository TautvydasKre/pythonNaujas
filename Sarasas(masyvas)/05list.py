m = [5 , 6, 8, 7, 14, 15, -85, -8, 13, 17]

# iteracija 1
# suma=0
# for i in m:
#     suma += i
#     i=10000
# print(suma)
# print(m)


#iteracija 2
suma = 0
for i in range(len(m)):
    suma += m[i]
    m[i] = 10000

print(suma)
print(m)