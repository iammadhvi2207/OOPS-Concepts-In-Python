class Car:
    def __init__(self, brand, speed):
        self.brand=brand
        self.__speed = speed

    def show_speed(self):
        return f"{self.brand} has the speed {self.__speed}ph"

c1= Car("Toyota", 180)
print(c1.show_speed())