class employee:
    start_time="Morning 9"
    end_time="Evening 5"

class adminStaff(employee):
    def __init__(self,role):
        self.role=role

class Accountant(adminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary
       


a1=Accountant(25000,"Manager")
print(a1.start_time,a1.end_time,a1.salary,a1.role)