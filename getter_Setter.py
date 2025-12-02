class bank:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance # 2 underscore=private and 1=protected

    def get_balance(self):  #getter
        return self.__balance

    def set_balance(self,newBalance): #setter
        self.__balance=newBalance

c1=bank("Abhi",100_000)
c1.set_balance(200_000)
print(c1.name,c1.get_balance())

print(c1._bank__balance) # accessing private attribute via objName and className (not recommended)