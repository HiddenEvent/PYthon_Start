# - 형변환 문제
x, y, z = '100', 10.5, 20

# - 1
print(int(x)+y)
print(x+str(z))
print(str(y)+str(float(z)))
print(str(int(x)+y)+str(z))

a, b = map(int, input().split())
print(a+b)