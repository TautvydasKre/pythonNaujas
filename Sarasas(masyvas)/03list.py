m = [5 , 6, 8, 7, 14, 15, -85, -8, 13, 17]
a = m.copy()
print(id(m))
print(id(a))
dalisList = m[1:5:2]#NUO PIRMO IKI PENKTO ZINGSNIU 2
print(dalisList)
b=m[0:-1]
print(b)
c = m [0:len(m)]
print(c)
d = m[::] #kopija viso
print(d)