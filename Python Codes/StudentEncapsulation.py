class Student:
    def __init__(self, marks) :
        self.__marks=marks

    def display(self) :
        return self.__marks

s1=Student(45)
s2=Student(65)
print(s1.display())
print(s2.display())