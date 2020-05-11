import sys

data = sys.stdin.readline()
data = ord(data[0])
minVal1 = ord("A")
maxVal1 = ord("Z")
minVal2 = ord("a")
maxVal2 = ord("z")
if data >= minVal1 and data <= maxVal1:
    print(chr(data+32))
elif data >= minVal2 and data <= maxVal2:
    print(chr(data-32))
else :
    print("문자만 입력하세요")