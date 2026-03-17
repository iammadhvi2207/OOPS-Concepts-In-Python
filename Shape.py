class Shape :
    def draw(self):
        print("Drawing a shape")

class Circle(Shape) :
    def draw(self):
        print("Drawing a circle")

c1=Circle()
c1.draw()