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