from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class lion(animal):
    def make_sound(self):
        print("ROAR!")

class cow(animal):
    def make_sound(self):
        print("MOO!")

Lion=lion()
Lion.make_sound()

Cow=cow()
Cow.make_sound()

