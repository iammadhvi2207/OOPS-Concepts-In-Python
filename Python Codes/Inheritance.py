class Animal:
    def speak(self):
        print("Animals Make Sounds ")

class Dog(Animal):      # Inheritance
    def bark(self):
        print("Dog Barks !")

d=Dog()
d.speak()
d.bark()