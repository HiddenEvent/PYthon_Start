# 문자열 연산

# - 인덱싱
#  1) 파이썬에서는 문자열이 + , *는 가능하다.
#  2) '+' '-'는 문자열 연산이다.
#  3) 양수, 음수를 전부 사용한다. 
#  4) 인덱스를 음수로 적을떄는 데이터의 끝부터 시작한다.... -1 부터 끝자리 시작

msg = "abcdef"

print(len(msg)) # 길이구하기

print(msg[0]) # ==== print(msg[-6]) 둘다 같다.

# 문자열 슬라이싱
#  1) 내가 지정한 범위 안의 문자열을 자르는 것
#  2) 인덱스값을 이용하여 문자열을 자른다.
#  3) 형식
#     변수명[인덱스 : 인덱스]
#     ex)  [0:4]  ==== 0번 인덱스 부터 4번 인덱스전까지....
#  4) 인덱스 범위가 잘못되면 슬라이싱을 하지 못한다...
print(msg[4:8])
print(msg[4:]) # 뒤 인덱스는 생략 가능(끝까지 출력한다)
print(msg[:3]) # 뒤 인덱스만 입력한 경우 끝인덱스 까지 출력한다