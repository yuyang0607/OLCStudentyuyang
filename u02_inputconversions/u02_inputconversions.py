# name = input("What is your name: ")
# hobby = input("What is your hobby: ")
# sentence = f"{name} likes {hobby}"
# print(sentence)

# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# result = num1 + num2
# print(result)

#------------------------------------------------------------
# Exercise 8: Area of a Circle with .format()
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using .format(). 
# Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."

pi = 3.14
radius = float(input("enter a radius for circle: "))
area = 3.14 * radius**27
print(f"The area of the circle is {area}")