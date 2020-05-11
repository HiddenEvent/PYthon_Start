import random
u = 1000 #강화
l = 0 #레벨
s = 35#성공
f = 30#실패
result = 0 # 현금

while l < 10:
    p = random.randint(0,100)
    print(p)
    if p < s :
        result = result + u
        l+=1
    elif p > 100-f :
        if l == 0 :
            result = result + u
        else:
            result = result + u
            l-=1

print(result)