dic = {'a':1,'b':2,'c':3}
print(type(dic))
print(len(dic))

print(dic['b'])
dic['b'] = 20
print(dic['b'])
print(dic)

for i in dic :
    print(i+" : ",dic[i])