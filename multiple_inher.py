class teacher:
    def __init__(self,salary):
        self.salary=salary
    
class student:
    def __init__(self,gpa):
        self.gpa=gpa

class TA(teacher,student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        student.__init__(self,gpa)
        self.name=name

TA1=TA(25000,7.00,"Abhi")
print(TA1.gpa,TA1.name,TA1.salary)