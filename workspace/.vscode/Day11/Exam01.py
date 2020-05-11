import random
i=1
b=0
for i in range(i,21):
    a = random.randint(100,1000)
    print(str(i)+"번째 :"+str(a))
    b+=a
print(str(b)+"만원 가져라")