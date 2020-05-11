import sys
def pyMax(*numbers):
    print(numbers)
    return max(numbers)

def pyMin(*numbers):
    print(numbers)
    return min(numbers)



def init():
    numbers = list(map(int, sys.stdin.readline().split()))
    maxNum = pyMax(numbers)
    minNum = pyMin(numbers)
    print(maxNum)
    print(minNum)

init()