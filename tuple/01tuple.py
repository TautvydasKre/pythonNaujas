kort = (5, 9, 9, 7, 9, 7)
print(kort)
print(type(kort))
print(kort[1])
sar = ([4,8,7])
sar[1] = 15
print(sar)
# kort[1] = 20
# tuple yra greitesnis uz list (greiciau apdorojamas , iteruojamas it t.t)
person=('Jonas','Petraitis', 375102105874)
taskas =(4, 8)
taskasA = 4, 8, 9
print(type(taskasA))
listA = list(taskasA)
print(type(listA))
print(kort[1]+5)
x1 , x2 , x3 , x4, x5 , x6 = kort
print(type(x1))
sar1=[]
for i in range(len(kort)):
    sar1.append(kort[i]+i)
print(sar1)
print(kort)

print(kort.count(9))
print(kort.index(9))
kort+=(1,1,1)
print(kort)
kitasKort = kort
print(kitasKort)
print(id(kort))
print(id(kitasKort))
kitasKort+=(1,1,1)
print(kort) 
print(kitasKort)
print(id(kort))
print(id(kitasKort))