def isEven(a):
    return a%2 == 0


while True:
    a = int(input("정수입력"))
    if a==0:
        print("Bye~*")
        break
    answer = isEven(a)
    if(answer) :
        print("짝수")
    else:
        print("홀수")