# how to define a list - planets

# define a list
# planets = ["mercury", "venus", "earth", " mars", "jupiter", "saturn", "uranus", "neptune"]

# # retrieve the value from a list
# print(planets[2]) # earth

# # replace value in a list
# planets[3] = "Denzelland"
# print(planets) # to prove

# # remove item from list
# del planets[6]
# print(planets)

# # remove item using name
# planets.remove("mercury")
# print(planets) # to prove

# # add to a list
# planets.append("jiajieland")
# print(planets) # to prove

# # how many items there are in the list
# count = len(planets)
# print(count)

# # how to loop through a list
# for i in planets:
#     print(f"Someday I would like to visit {i}")

##############################################################
# write a program to ask for the student"s name

# Assume you have 5 students

# add each name to the list

# loop through the list and make a greeting
# example
# Hello Deborah 
# Hello Marcus
#......

# students = [] # empty list

# for i in range(5):
#     name = input("Enter student's name: ")

#     # how to add the name to the list??
#     # list = students.append(name)
#     students.append(name)

# for i in students:
#     print(f"Hello {i}")

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 9: Summing Numbers in a List
# Write a program to calculate the sum of numbers in a list.
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]


#### find the total of all the numbers

##### find the average of this list of numbers

#### find the biggest number in this list

#### find the smallest number in this list

# total = sum(list1)
# print(total)

# average = total / len(list1)
# print(average)

# maxnum = max(list1)
# print(maxnum)

# minnum = min(list1)    
# print(minnum)

###############---------------
# another method

total = 0
for i in list1:
    total = total + i
print(total)

average = total/len(list1)
print(average)

maxnum = 0
#####################################################################################
# string variable
# integer, float
# boolean >> True False

# List
###################################################
# Part 1: Learning Exercises

# Exercise 1: Accessing List Elements by Index
# Write a program to access and print the first, second, and last 
# elements of a list using indexing.

# fruits = ["apple", "banana", "cherry", "date"]
# print(f"{fruits[0]}")
# print(f"{fruits[1]}")
# print(f"{fruits[-1]}")
#------------------------------------------------------------
# Exercise 2: Adding Elements to a List
# Write a program to add an element to the end of a list using 
# append(), and add another element at a specific index using 
# insert().

# fruits = ["apple", "banana", "cherry", "date"]
# fruits.append("orange")
# fruits.insert(-2, "durian")
# print(fruits)
#------------------------------------------------------------
# Exercise 3: Using del() to Remove an Element by Index
# Write a program to delete an element at a specific index.
# Example: Remove the second color.

# fruits = ["apple", "banana", "cherry", "date"]
# del fruits[1]
# print(fruits)
#------------------------------------------------------------
# Exercise 4: Using remove() to Remove an Element by Value
# Write a program to remove a specific element by its value.
# Example: Remove "green" from the list.
# colors = ["red", "green", "blue", "yellow"]
# colors.remove("green")  # Remove by value
# print("Colors after removal: {}".format(colors))

# colors = ["red", "green", "blue", "yellow"]
# colors.remove("")
# print(colors)
# #------------------------------------------------------------
# Exercise 5: Using pop() to Remove and Retrieve an Element
# Write a program to remove the last element of a list using pop().
# Example: Remove and print the last color.
# colors = ["red", "green", "blue", "yellow"]
# removed_color = colors.pop()  # Remove the last element
# print("Removed color: {}".format(removed_color))
# print("Colors after pop: {}".format(colors))

# colors = ["red", "green", "blue", "yellow"]
# removed_color = colors.pop()
# print(colors)
#------------------------------------------------------------
# Exercise 6: Modifying Elements in a List
# Write a program to change the second element in a list to "pink."
# colors = ["red", "green", "blue"]
# colors[1] = "pink"  # Modify value at index 1
# print("Modified colors: {}".format(colors))

# colors = ["red", "green", "blue"]
# colors[1] = "pink"
# print(colors)
#------------------------------------------------------------
# Exercise 7: Membership Check
# Write a program to check if "blue" is in the list.
# colors = ["red", "green", "blue"]

# colors == True

# colors = ["red", "green", "blue"]
# if "blue" in colors:
#     print("blue is in the list")
# else:
#     print("blue is not in the list")
# validation check = existence check
#------------------------------------------------------------
##### to loop through every single item
# Exercise 8: Iterating Through a List
# Write a program to print each fruit in a list using a for loop.

# fruits = ["apple", "banana", "cherry", "date"]
# for i in fruits:
#     print(f"I like to eat {i}")