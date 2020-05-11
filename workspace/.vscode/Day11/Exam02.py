import sys

T = int(sys.stdin.readline()) #분 입력
s = T * 60
for s in range(s,-1,-1):
    print(str(s//60)+"분"+str(s%60)+"초 남음")