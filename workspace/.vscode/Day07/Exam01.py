import random

a = int(random.random() * 100) + 1
print(a)

b = int(random.random() * 900) + 100
print(b)

c = int(random.random() * (ord("Z")-ord("A"))) + ord("A")
print(chr(c))

d = int(random.random() * 99 ) + 1
print(d)
if d%2==0:
    print("True")
else:
    print("false")