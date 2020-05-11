import sys, random

menu = {'칼국수':6000,'비빔밥':5500,
        '돼지국밥':7000,'돈까스':7000,'김밥':2000,'라면':2500}

# 2.
# for i in menu :
#     if menu[i] < 6000:
#         print(i+" : ",menu[i])

# 3.
# selc = input("메뉴입력")
# check = menu.get(selc)
# if check == None :
#     menu.update({selc:input("가격입력 : ")})
# else :
#     menu[selc] = input("동일 메뉴 존재 가격입력 : ")
# selc = input("메뉴입력")
# if selc in menu:
#     menu[selc] = input("동일 메뉴 존재 가격입력 : ")
# else :
#     menu.update({selc:input("가격입력 : ")})
# print(menu)

selc = input("메뉴입력")
menu.update({selc:input("가격입력 : ")})
print(menu)
#4.
# ran = int(random.randrange(len(menu)))
# i = 0
# for m in menu:
#     if ran == i :
#         print(m+ " : ",menu[m])
#     i += 1


# for i in dic :
#     if dic[i] < 6000
#     print(dic[i])
#     for k in dic[i] :
#         print(dic[i][k])