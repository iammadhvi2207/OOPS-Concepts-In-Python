class Employee :
    def __init__(self, name, salary):
        self.name=name
        self.__salary=salary

    def increase(self, amount):
        self.__salary +=amount

    def display(self):
        print(f"Salary : {self.__salary}" )

e1=Employee("Harshy", 3000000)
e1.increase(3000)
e1.display()