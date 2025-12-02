class animal:
    def __init__(self,name):
        location="ind"
        self.name=name

    def speak(self):
         print("Animal sound")

class dog(animal):
    def speak(self):
        super().speak()
        print("dog speak")

D=dog("Bruno")
D.speak()
# print(D.location)