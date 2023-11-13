m = [5 , 6,1,2, 8, 7, 14, 15,2,2, -85, -8, 13, 17]
did = max(m)#didziausias skaicius masyve
print(did)
maz= min(m)#maziausias skaicius masyve
print(maz)

mazEl = m[0]
# for i in range(1, len(m)):
#     if mazEl>m[i]:
#         mazEl = m[i]
# print(mazEl)
for i in m:
    if mazEl>i:
        mazEl = i
print(mazEl)

suma = sum(m)
print(suma)
#m.sort()
print(m)

m.reverse()
print(m)

m.sort(reverse=True)
print(m)

el = m.pop()
print(el)
print(m)
el2 = m.pop(2)
print(el2)
print(m)

m.remove(m[2])
print(m)

print(m.count(2))
print(m.index(2))