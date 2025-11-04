###################################################
# Part 1: Learning Exercises

# Exercise 1: A Simple Function
# Define a function that prints "Hello, World!" and call it.
# def greet():
#     print("Hello, World!")

# # Call the function
# greet()

# def hello():
#     print("hello world")

# hello()
#------------------------------------------------------------
# Exercise 2: Function with One Parameter
# Define a function that takes a name as a parameter and greets the user.
# def greet_user(name):
#     print("Hello, {}!".format(name))

# # Call the function with your name.
# greet_user("Alice")

# def greet(yourname):
#     print(f"Hello {yourname}")
# greet("Heng Hyi")
#------------------------------------------------------------
# Exercise 3: Function with Two Parameters
# Define a function that takes two numbers and prints their sum.
# def add_numbers(num1, num2):
#     print("The sum of {} and {} is {}".format(num1, num2, num1 + num2))

# # Call the function with two numbers.
# add_numbers(5, 10)

# def intro(yourname, myname):
#     print(f"Hello {yourname}, I am {myname}")

# intro("Matthias", "Savvy")
#------------------------------------------------------------
# Exercise 4: Function with a Return Value
# Define a function that calculates the area of a rectangle.
# def calculate_area(length, width):
#     return length * width

# # Call the function and store the result.
# area = calculate_area(5, 3)
# print("The area of the rectangle is {}".format(area))

# def add(num1, num2):
#     assume that both num1 and num2 are integers
#     answer = num1 + num2
#     print(f"{num1} + {num2} = {answer}")
# add(34, 98)
#------------------------------------------------------------
# Exercise 5: Using Returned Values in Further Computations
# Define a function that calculates the perimeter of a rectangle.
# def calculate_perimeter(length, width):
#     return 2 * (length + width)

# # Use both functions to calculate the area and perimeter.
# length = 6
# width = 4
# area = calculate_area(length, width)
# perimeter = calculate_perimeter(length, width)
# print("For a rectangle of length {} and width {}:".format(length, width))
# print("Area: {}, Perimeter: {}".format(area, perimeter))

# def area_rectangle(length, breadth):
#     area = length * breadth

#     return area
#calculate the total area of 5 rectangles
# length1 = 34, breadth1 = 26
# length2 = 36, breadth1 = 63
# length3 = 69, breadth1 = 66
# length4 = 97, breadth1 = 78
# length5 = 24, breadth1 = 68

# lengths = [34, 36, 69, 97, 24]
# breadth = [26, 63, 66, 78, 68]

# area_1 = area_rectangle(34, 26)
# area_2 = area_rectangle(36, 63)
# area_3 = area_rectangle(69, 66)
# area_4 = area_rectangle(97, 78)
# area_5 = area_rectangle(24, 68)
# total = area_1 + area_2 + area_3 + area_4 + area_5
# print(total)
# trace the line execution
# 81, 70, 71, 72, 81, 82, 70, 71, 72, 82 
#------------------------------------------------------------
# Exercise 6: Demonstrating Local and Global Variables
# Define a function that modifies a local variable.
# def local_variable_example():
#     x = 10  # Local variable
#     print("Inside the function, x is {}".format(x))

# # Outside the function.
# x = 20  # Global variable
# local_variable_example()
# print("Outside the function, x is {}".format(x))

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Greeting Multiple Users
# Write a function that takes a list of names and greets each one.
# Call the function with a list of names.
# greet_users(["Alice", "Bob", "Charlie"])

friends = ["Alice", "Bob", "Charlie"]
def greet_users(Alice, Bob, Charlie):




#------------------------------------------------------------
# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.


# Test the function with multiple operations.
# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))








#------------------------------------------------------------