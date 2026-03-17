# import random
# random.random() # gives a random number between 0 and 1
# random.randint(1, 10) # gives a random integer between 1 and 10
# random.choice([1, 2, 3, 4, 5]) # gives a random element from the list
# random.shuffle([1, 2, 3, 4, 5]) # shuffles the list in place
# random.sample([1, 2, 3, 4, 5], 3) # gives a random sample of 3 elements from the list
# random.randrange(1, 10, 2) # gives a random odd integer between 1 and 10

#import datetime
# datetime.datetime.now() # gives the current date and time
# datetime.date.today() # gives the current date
# datetime.timedelta(days=7) # gives a time delta of 7 days
# datetime.datetime.strptime("2022-01-01", "%Y-%m-%d") # converts a string to a datetime object
# datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d") # converts a datetime object to a string

# import math
# print("Square root of 16:", math.sqrt(16)) # gives the square root of 16
# print("Factorial of 5:", math.factorial(5)) # gives the factorial of 5
# print("Floor of 3.7:", math.floor(3.7)) # gives the floor of 3.7
# print("Ceiling of 3.7:", math.ceil(3.7)) # gives the ceiling of 3.7
# print("Pi:", math.pi) # gives the value of pi
# print("5 raised to the power of 3:", math.pow(5, 3)) # gives 5 raised to the power of 3
# print("Absolute value of -5:", math.fabs(-5)) # gives the absolute value of -5

# import random
# print("Random number between 1 and 10:", random.randint(1, 10)) # gives a random integer between 1 and 10
# print("Random number between 0 and 1 :", random.random()) # gives a random number between 0 and 1
# print("Random choice from list:", random.choice([10, 20, 30, 40, 50])) # gives a random element from the list
# print("Shuffled list:", random.shuffle([1, 2, 3, 4, 5])) # shuffles the list in place
# print("Random Even Number Between 2 and 20:", random.randrange(2, 21, 2)) # gives a random even integer between 2 and 20
# print("5 random numbers between 10 and 100:", random.sample(range(10, 101), 5)) # gives a random sample of 5 elements from the range 1 to 100

# import datetime
# print("Current date and time:", datetime.datetime.now()) # gives the current date and time
# print("Current date:", datetime.date.today()) # gives the current date
# today = datetime.date.today()
# print("Year  :", today.year, "Month:", today.month, "Day:", today.day) # gives the current year, month and day
# now = datetime.datetime.now()
# formatted = now.strftime("%Y-%m-%d %H:%M:%S %p") # converts a datetime object to a string
# print("Formatted date and time:", formatted)

print("-----------------------------------------------------------------------------")

import Calculator as cal # imports the Calculator module and gives it the alias 'cal'
# created by me
print(cal.add(5, 3)) # gives the sum of 5 and 3
print(cal.subtract(5, 3)) # gives the difference of 5 and 3
print(cal.multiply(5, 3)) # gives the product of 5 and 3
print(cal.divide(5, 3)) # gives the quotient of 5 and 3
l = [1, 2, 3, 4, 5, 5, 6, 6]
print("Unique elements in the list:", cal.unique(l)) # gives the unique elements in the list
print("-----------------------------------------------------------------------------")

# There are several ways to import a module in Python. 
# 1. import module_name: This imports the entire module and you can access its functions using the module name as a prefix. For example, import math allows you to use math.sqrt() to access the square root function.
# 2. from module_name import function_name: This imports a specific function from the module and allows you to use it directly without the module name prefix. For example, from math import sqrt allows you to use sqrt() directly to access the square root function.
# 3. from module_name import *: This imports all functions from the module and allows you to use them directly without the module name prefix. For example, from math import * allows you to use sqrt() directly to access the square root function, but it can lead to name conflicts if there are functions with the same name in different modules.
# 4. import module_name as alias: This imports the entire module and gives it an alias that you can use to access its functions. For example, import math as m allows you to use m.sqrt() to access the square root function. 

import temp_converter as temp 
# created by me
print(temp.c_to_f(25))
print(temp.f_to_c(77)) 
print('-' * 77)

import area_module as area
# created by me
print("Area of a circle with radius 5:", area.area_of_circle(5))
print("Area of a rectangle with length 10 and width 5:", area.area_of_rectangle(10, 5))
print("Area of a triangle with base 10 and height 5:", area.area_of_triangle(10, 5))
print('-' * 77)

