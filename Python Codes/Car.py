class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.color} {self.brand} is starting ...")

car1 = Car("Tesla", "Blue")
car2 = Car("Toyota", "Red")
car3 = Car("Ford", "White")

car1.start()
car2.start()
car3.start()