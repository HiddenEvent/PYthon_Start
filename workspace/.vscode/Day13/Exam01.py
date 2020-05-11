import sys

menu = (('칼국수', 6000), ('비빔밥', 5500), ('돼지국밥', 7000), ('돈까스', 7000), ('김밥',2000), ('라면', 2500))
result = 0

for i in range(0,len(menu)):
    if menu[i][0] == '김밥':
        result = menu[i][1]
        print("1. 김밥가격 : "+str(result))
    elif menu[i][0] == '라면':
        result = menu[i][1]
        print("1. 라면가격 : "+str(result))


menuResult = ""
for i in range(0,len(menu)):
    if menu[i][1] == 7000:
       menuResult += menu[i][0]+" "
print("2. 매뉴 : "+menuResult)

for i in range(0,len(menu)):
    if menu[i][1] <= 6000:
       menuResult += menu[i][0]+" "
print("3. 6000 이하 : "+menuResult)

selec = sys.stdin.readline()
selec = selec[0:-1]

for i in range(0,len(menu)):
    if menu[i][0] == selec :
        
        print("4. 선택한 메뉴의 각격은 : "+str(menu[i][1]))


selec = ""
while True:
    flag = 0
    selec = sys.stdin.readline()
    selec = selec[0:-1]
    if selec == "exit":
        break
    for j in range(0,len(menu)):
        if selec == menu[j][0]:
            flag = 1
            print("5. 가격은 :"+str(menu[j][1]))
    if flag == 0 :
        print("다시입력해주세요")
            
            
    
