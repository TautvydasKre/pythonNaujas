aibeA=set()
print(type(aibeA))
aibeB = {}
print(type(aibeB))
aibeC = {1,8,9,7}
print(type(aibeC))
# aibiou elementai neturi indexu
# print(aibeC[0]) #nepavyks
for i in aibeC:
    print(i)
aibeC.add(11)
print(aibeC)
aibeC.add(11)
print(aibeC)
sar = [1, 8, 4, 1, 4, 1, 8, 5, 8, 1, 8, 1, 7, 1, 1, 7]
aibeD = set(sar)
print(aibeD)

print(1 in aibeD) # patikrina ar aibeja yra nurodytas elementas
