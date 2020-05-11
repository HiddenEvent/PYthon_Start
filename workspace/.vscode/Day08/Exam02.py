import sys

a = int(sys.stdin.readline())#짜장 갯수
b = int(sys.stdin.readline())#짬뽕 갯수
black = 5000 #짜장
red = 6000  #짬뽕
absum = a+b
amount = a*black+b*red
if absum >= 5:
    print(amount = amount-3000)
if absum >= 10:
    print(int(amount*0.9))
if absum <5:
    print(amount)