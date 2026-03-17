class Employee :
    company = "Google"

    def __init__(self, name, salary) :
        self.name = name
        self.salary = salary

e1= Employee("Kirti", 100000)
e2= Employee("Khushi", 200000)  

print(e1.name, e1.salary, e1.company)
print(e2.name, e2.salary, e2.company)