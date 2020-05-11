# 모듈 - 어떠한 기능을 미리 구현해 놓은 것....
#  1) 오픈소스 - 사용자가 구현한 코드를 배포하여 여러사람에게 공유하며 발전해 나가는 방식
#  2) 왠만한 기능들은 모두 구현되어 있다.
#  3) 만들어진 기능을 찾아서 가져다 사용하기만 하면 된다.
 
# - 사용형식
#  1) import 모듈명
#  2) from 모듈명 import 변수명이나 함수명  ★ 이런형식은 사용하지 말자 겹칠수 있음....
# random - 임의의 수를 구하는 함수들이 모여 있는 모듈.....
# random() - 임의의 수를 구하는 함수
import random

#print(random.random())

# from random import random
# print(random())

#내가 원하는 범위 안의 수 구하지...
# - int(random.random() * 범위 안에 수의 개수) + 시작수
#ran = int(random.random() * 2) + 8
#print(ran)
a = random.random()
b = a * 2
c = int(b) # 0 ~ 1
d = c + 8 # 8 ~ 9
print(a)
print(b)
print(c)
print(d)