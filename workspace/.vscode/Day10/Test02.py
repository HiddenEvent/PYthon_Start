import random , sys


f = 0
scr = 0
while f < 3 :
    l = random.randint(2, 19)
    r = random.randint(1, 9)
    print(str(l)+" X "+str(r)+"의 답은? ")
    answer = int(sys.stdin.readline())
    if answer == l*r :
        if l < 11 :
            scr += 10
        else :
            scr += 15
    else :
        f +=1
        print("ㄴㄴ")
print(scr)