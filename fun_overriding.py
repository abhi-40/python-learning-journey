class employee:
    def get_designation(self):
        print("designation= Employee")

class teacher(employee):
    def get_designation(self):
        print("Designation=Teacher")

t1=teacher()
t1.get_designation()