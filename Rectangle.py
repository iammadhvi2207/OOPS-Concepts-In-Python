class Rectangle : 
    def __init__(self, length, breadth) :
        self.length = length
        self.breadth = breadth

    def area(self) :
        return self.length * self.breadth

rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 4)

print(f"Area of Rectangle 1: {rect1.area()}")
print(f"Area of Rectangle 2: {rect2.area()}")