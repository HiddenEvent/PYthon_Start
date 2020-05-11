import sys
N = int(sys.stdin.readline())
i = 1
answer = ""
while i <= N :
    if N%i == 0:
        answer = answer+str(i)+" " 
    i+=1
print(answer+"이 약수임"  )

i=1
result = 1
while True:
    N = int(sys.stdin.readline())
    if N >= 10 and N <= 20 :
        while i <= N :
            result = result+i
            i += 1
        break
    else :
        print("10~20 범위안 숫자입력 다시입력")
print(result)