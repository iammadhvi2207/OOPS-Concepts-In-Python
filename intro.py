# # Dynamic Language {It will identify the the type automatically}
# x = 10              # Integer
# y = 20.5            # Float
# name = "Madhvi"     # String

# Type Casting {Mostly Logical Errors}
# Conditional Statements

# x=10
# if x>5:
#     print("A")
# else:
#     print("B")
# x=()
# if x:
#     print("True")
# else:
#     print("False")

# marks = 85

# if marks >= 60 :
#     print("Pass")
# if marks >= 80 :
#     print("Good")
# else:
#     print("Fail")

# age = 25
# if age > 18 & age < 60:
#     print("Valid")

# Loops ( Iterative Statements )
# while conditions:
#     Statements
# for Var in range ():
#     Statements

# i=1
# while i<=5:
#     print(i)
#     i+=1

# for i in range (1,6):
#     pass

# for i in range(1,6): {in : this is a membership operator} {in : this is a keyword here}
#     if i%2 !=0 :
#         print (i)

# {Pass Keyword : is used to avoid syntax error when no code is to be executed}

# def add(a,b): #{this function is void function}
#     print(a+b)

# c=10
# result= c+add(3,4)
# print(result)

# def print_even(n):
#     for i in range(1,n+1):
#         print(i*2)

# def power(base, exp=2):
#     return base ** exp {** - exponent operator}
# print(power(3))

# # How to print all the numbers divisible by 3 and 5 between a range of 1 to 100
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)

# # A function that returns senior if the age is greater than 60 else returns junior
# def age_group(age):
#     if age>60:
#         return "Senior"
#     else:
#         return "Junior"

# print(age_group(65))
# print(age_group(45))

# # Count how many numbers are divisible by 4 in between 1 to 50.
# count =0
# for i in range(1,51):
#     if i%4==0:
#         count+=1
# print(count)

# # Function that print N even Numbers
# def print_even(n):
#     for i in range(1,n+1):
#         print(i*2)

# print_even(5)

# def test(x):
#     if x> 10:
#         return x*2
#     return x+2
# print(test(5))
# print(test(15))

# # List_name = [items]
# List1=[1, "JD", "Harshy", 3.14, True]
# print(List1)
# List1.append("Maddy") # {append is used to add an element at the end of the list}
# print(List1)
# List1.insert(2,"Stark") # {insert is used to add an element at a specific index}
# print(List1)
# List1.remove(1) # {remove is used to remove an element from the list}
# print(List1)
# List1.pop() # {pop is used to remove the last element from the list}
# print(List1)
# List1.pop(2) # {pop is used to remove an element from a specific index}
# print(List1)
# List1[0]="Jaidev"
# print(List1)
# print last element: print(list1[-1])

# nums = [5, 10, 15, 3.4, "Maddy" ] #{Looping for Data / For Each Loop} 
# var=[]
# var1=""
# for i in nums:
#     var.append(i)
#     var1+=str(i) + " "
# print(var)
# print(var1)

# dictname = {    {Syntax for Dictionary} {This is Important} 
#     key1 : value,
#     key2 : value1
# }

# my_name = {
#     "name" : "Madhvi",
#     "age" : 22,
#     "Course" : "B.Tech"
# }

# print(my_name["name"])

# var = list(my_name.keys()) {to display one key at a time}
# print(var[0])

# students = [
#     {"name" : "Madhvi", "marks" : 100},
#     {"name" : "Harshy", "marks" : 90},
#     {"name" : "Jaidev", "marks" : 25}
# ]

# for s in students: 
#     if(s["marks"] >=60):
#         print(s["name"])

my_name = {
    "name" : "Madhvi",
    "age" : 22,
    "Course" : "B.Tech"
}

# for key,val in my_name.items(): # {items() is used to get the key and value of the dictionary}
#     if val=="B.Tech":
#         print(key)
# v= input("Enter the value to search for: ")
# keys = [key for key,val in my_name.items() if val== v] # {List Comprehension}
# print(keys)

# def get_key(value):                  #{Try-Except Block} {Exception Handling}
#     try:  #Risky Code 
#         for key, val in (my_name.items()):
#             if val==value:
#                 return key
#         raise Exception
#     except Exception:
#         return "Value not Found"

# print(get_key("B.Tech"))
# print(get_key(221))



