# #Encapsulation is one of the major reasons of using OOPS in Python. As it Groups similar data Together.
class Make_up(): #Syntax class ClassName():  {No Memory is Allocated for a class until an Object is Created.}
    tax_amt = 1.18
    def __init__(self,first,last,product,price): #Constructor is a special method which is used to initialize the attributes of the class. 
        self.first=first    #Instead of this we USE self In Python.
        self.last=last
        self.product = product
        self.price = price

    def get_full_name(self):
        return '{} {}'.format(self.first,self.last)  #{}{}- these brackets are for creating space for variables.
        #Format() Method : this method is used to format the string. It takes the variables as arguments and replaces the placeholders in the string with the values of the variables.

    def final_price(self):
        return self.price * self.tax_amt  #Inheritance Inside A Class. We Checked for the tax_amt variable which is not in the fuction it goes outside to check function in the class and used it in the method final_price().

lady1 = Make_up("Kirti","Singh","Blush",300) #Creating an Object of the class . Memory is Allocated when the object is Created.
lady2 = Make_up("Khushi","Sharma","Contour",3000)


# print(lady1.get_full_name())
# print(lady2.get_full_name())

# # lady1.name = "Kirti's"
# # lady1.product = "Foundation"

# # lady2.name = "Khushi's"
# # lady2.product = "Lipstick"  

# # print(lady1.name)
# # print(lady2.product)

#Before Changing the Tax Value
print(f'Object 1: {lady1.final_price()}') #Another Way to print using F-
print(f'Object 2: {lady2.final_price()}')

#After Changing the Tax Value
lady1.tax_amt = 1.20
print(f'Object 1: {lady1.final_price()}')
print(f'Object 2: {lady2.final_price()}')

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 80:
#             return "B"
#         elif self.marks >= 70:
#             return "C"
#         elif self.marks >= 60:
#             return "D"
#         else:
#             return "F"

# student1 = Student("Madhvi", 95)
# student2 = Student("Harshy", 75)

# print(student1.name, student1.get_grade())
# print(student2.name, student2.get_grade())

