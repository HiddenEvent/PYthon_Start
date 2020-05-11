import sys

a = int(sys.stdin.readline())
if a%5 ==0:
    print("5의 배수입니다")
else:
    print("5의 배수 아님")

if a > 0 and a < 100 :
    print("정상")
else:
    print("비정상")

if a%3 == 0 and a%2 ==0:
    print(a)

b,c,d = map(int, sys.stdin.readline().split())
avg = (b+c+d)/3

if avg >= 60 :
    print("합격")
else:
    print("불합격")