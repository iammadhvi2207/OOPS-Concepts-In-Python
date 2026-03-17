class Bird :
    def fly(self):
        print("Flying")

class Sparrow(Bird) :     #Inheritancee
    def fly(self):
        print("Sparrow is flying")

s1 = Sparrow()
s1.fly()