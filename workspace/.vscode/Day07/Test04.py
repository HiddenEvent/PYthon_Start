import random

# randint == int(random.random() * 범위안에 숫자) + 시작수
#  - 내가 지정한 범위 안의 숫자를 구하는 수
#  - randint(a,b)
#  - a부터 b까지의 정수 중에 임의의 값을 생성하는 함수

a = 0

while a < 10:
    print(random.randint(5,9))
    a+=1



#65를 A로 변환 ... chr() 변환함수...
print(chr(65))

#A를 65로 변환... ord() - 문자를 정수값을 변환하는 함수
print(ord("A"))
