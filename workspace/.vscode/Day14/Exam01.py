import sys, random
menu = [['칼국수',6000],['비빔밥',5500],
        ['돼지국밥',7000],['돈까스',7000],['김밥',2000],['라면',2500]]

#1.
# for m in menu :
#     if m[0] == '비빔밥' or m[0] == '돈까스':
#         print(m[1])


#2.


while True:
    check = False
    a = input("메뉴 입력")
    for m in menu :
        if m[0] == a :
            print("메뉴중복 다시입력")
            check = True
            break
    if check :
        continue
    b = int(input("가격 입력"))
    break
menu.append([a,b])
print(menu)

# #3.
a = input("메뉴 입력")

check = True
for m in menu :
    if m[0] == a :
        check = False
        print("동일 메뉴 존재 가격만 입력"+m[0])
        b = int(input("가격 변경 입력"))
        m.pop(1)
        m.insert(1,b)
        break
if check :
    b = int(input("가격 입력"))
    menu.append([a,b])
# print(menu)
# #4.
# num = random.randint(0,len(menu))
# print(menu[num])