class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}")

student1 = Student("Madhvi", 20, 101)
student2 = Student("Harshy", 22, 102)

student1.display_info()
student2.display_info() 