class employee:
    start_time="Morning 9"
    end_time="Evening 5"

class Teachers(employee):
    def __init__(self,sub):
        self.sub=sub

class adminStaff(employee):
    def __init__(self,role):
        self.role=role

t1=Teachers("Maths")
print(t1.start_time,t1.end_time,t1.sub)

a1=adminStaff("Manager")
print(a1.start_time,a1.end_time,a1.role)