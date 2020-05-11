import sys

valList = []
tempList = []
for i in range(0,10):
    valList.append(int(sys.stdin.readline()))

for j in range(0,len(valList)):
    temp = valList[j]%42
    
    if temp in tempList:
        pass
    else:
        tempList.append(temp)

print(len(tempList))