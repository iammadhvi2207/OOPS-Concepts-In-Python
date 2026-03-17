class Employee : 
    def __init__(self, name, salary) :
        self.name = name
        self.salary = salary

    def calculate_bonus(self) :
        return self.salary * 1.1

employee1 = Employee("Madhvi", 50000)
employee2 = Employee("Harshy", 60000)

print(f"Employee: {employee1.name}, Salary: {employee1.salary}, Bonus: {employee1.calculate_bonus()}")
print(f"Employee: {employee2.name}, Salary: {employee2.salary}, Bonus: {employee2.calculate_bonus()}")