class Vehicle :
    def __init__(self, type):
        self.type = type

class Bike(Vehicle) :
    def __init__(self, type, brand):
        super().__init__(type)
        self.brand = brand

    def display_info(self):
        print(f"Type: {self.type}, Brand: {self.brand}")

bike1 = Bike("Motorcycle", "Yamaha")
bike2 = Bike("Scooter", "Honda")

bike1.display_info()
bike2.display_info()