#가변인자( * )  -> 튜플타입이됨
def total(*tot):
    hap = 0
    for i in tot:
        hap+=i
    print(hap)

total(1,2,3,4,5,6,7)

#키워드 가변인자( ** )  -> 딕셔너리형 타입으로 저장됨
def disp(**keyword):
    print(keyword)

disp(a=10,b=20,c=30)