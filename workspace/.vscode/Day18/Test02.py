class Info:
    __name = None
    __age = None

    def __init__(self):
        pass

    def setName(self,name):
        self.__name
    
    def setAge(self,age):
        if age < 1 :
            self.__age = 1
            return
    
    def disp(self):
        print("이름 : {}".format(self.__name))
        print("나이 : {}".format(self.__age))

in1 = Info()

in1.__name = ""

in1.setName = "김동혁"
in1.setAge = -20