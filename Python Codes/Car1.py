class Car :
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Price: {self.price}")

car1 = Car("Toyota", 20000)
car2 = Car("Honda", 25000)

car1.display_info()
car2.display_info()