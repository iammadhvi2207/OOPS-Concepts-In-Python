class Employee : 
    def __init__(self, salary):
        self.salary = salary

class Manager(Employee) :
    def __init__(self, salary):
        super().__init__(salary)

    def add_bonus(self):
        return self.salary * 1.10

e1= Manager(50000) 
print(f"Manager Salary: {e1.salary}, Bonus: {e1.add_bonus()}")