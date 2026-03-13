class Student :
    def __init__(self, name, roll_no): 
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

student1 = Student("Madhvi", 101)
student2 = Student("Harshy", 102)

student1.display_info()
student2.display_info()