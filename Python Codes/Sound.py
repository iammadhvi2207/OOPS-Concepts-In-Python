class Cat :
    def sound(self):
        print("Meow")

class Dog(Cat) :
    def sound(self):
        print("Woof")

c1 = Cat()
d1 = Dog()
c1.sound()
d1.sound()