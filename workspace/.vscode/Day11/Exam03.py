import random

# 1
for i in range(1,51):
    if(i%5 == 0):
        print(i)
    else :
        print(i, end='\t')

# 2
st = "Python basic program language"
st2 = ""
for i in range(0,len(st)):
    if st[i] == " ":
        continue
    else:
        st2 += st[i]
print(st2)

# 3
st = ""
for i in range(0,10):
    st += chr(random.randint(ord("A"),ord("Z")+1))
print(st)

# 4
st = ""
a = random.randint(0,ord("Z")+1)
random.randint(ord("A"),ord("Z")+1)
random.randint(ord("a"),ord("z")+1)
random.randint( 0, 10)
