class employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def print_info(self):
        info= f"the name is: {self.name} and the salary is: {self.salary}"
        print(info)

    @staticmethod
    def sum(a,b):
        return a+b

    @classmethod
    def print_company(clz):
        print(clz.company)

    @classmethod
    def changeCompany(clz,new_company):
        clz.company=new_company


e1=employee("abhi",6798)
e2=employee("aman",2345)

e1.print_info()
e2.print_info()

print(e1.sum(23,56))
(e1.changeCompany("ACER"))
e1.print_company()
# print(employee.company)