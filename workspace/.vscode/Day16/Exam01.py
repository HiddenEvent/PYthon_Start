
starFuncCount = int(input("출력 횟수 입력 : "))

def star(a):
    return "★"*a

def main():
    print(star(starFuncCount))
    print(star(5))
    print(star(6))
    print(star(7))
    return exit(0)

main()
