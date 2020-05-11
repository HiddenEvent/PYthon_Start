import sys
count = 0
maxVal = 100 # 최대값
minVal = 1   # 최소값
answer = int(sys.stdin.readline()) #정답


while True :
    if answer > maxVal or answer <minVal:
        print("다시입력")
        answer = int(sys.stdin.readline()) #정답
    else :
        count += 1
        a = int(sys.stdin.readline())
        if a == answer :
            print("OK")
            break
        elif a > answer :
            print("down 다시입력")
        elif a < answer :
            print("up 다시입력")
print(count)