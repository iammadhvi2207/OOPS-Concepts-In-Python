class Person:
    def __init__(self,  age):
        self.__age = age

    def Show_age(self):
        return f"I am {self.__age} years old."

p1 = Person(25)
print(p1.Show_age())