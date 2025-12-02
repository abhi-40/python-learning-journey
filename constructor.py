class employee:
    def __init__(self,salary,name,bond):
        self.salary=salary
        self.name=name
        self.bond=bond

    def get_salary(self):
        return self.salary

    def printInfo(self):
        print(f"the name is: {self.name}. Salary is: {self.salary}.Bond is of {self.bond}")

e1=employee(3400,"Abhishek","4 Years")
e1.printInfo()