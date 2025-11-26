# compare 2 numbers to see which one is bigger
# num1 = 10
# num2 = 20

#use if condition
# if num1 > num2:
#     # if the above condition is true, run this code
#     print(f"{num1} is more than {num2}")

# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")

# else:
#     #if the above condition is false, run this code
#     print(f"{num1} is not more than {num2}")

#PASSWORD PROGRAM
# password = "Password123"
# for i in range(3):
#     inputpassword = input("Enter a password: ") # ask user to enter a password
#     if i != password:
#         print("Access denied")
#         break # breaks out of loop
#     else:
#         print("Access granted")




### RANDOM NUMBERS 
# import random 
# marks = 0
# for i in range(30):
#     num1 = random.randint(20, 50) # generating a random number between 20 and 50
#     print(num1)

# ### TASK: MAKE A MATH QUIZ

# for i in range(10):
#     # generate 2 random numbers
#     num1 = random.randint(20, 50) # generate 1st random number #20
#     num2 = random.randint(20, 50) # generate 2nd random number #30

#     # ask the student to answer
#     # What is 20 + 30 ?
#     answer = int(input(f"What is {num1} + {num2}? "))

#     # check if the student enter the correct answer
#     if answer == num1 + num2:
#         print("Correct.")
#         marks = marks + 1
#         #marks += 1
#     else:
#         print("Wrong.")

# # tell the student their marks
# print(f"You scored {marks} out of 10.")













































# import random
# marks = 0
# num1 = random.randint
# answer =
# for i in range(10):
#     if answer == num1 + num2:















#################################
# RANDOM NUMBER GUESSING PROGRAM

# Generate a random number

# import random
# print("Guess my number from 1 to 100!")
# rannum = random.randint(1, 100)
# # need to loop for 7 times

# # input the number
# for i in range(7):
#     guess = int(input("Guess a number: "))
# # check if bigger or smaller


# # bigger
#     if guess > rannum:
#         print(f"Your guess {guess} is too big.")
#     # smaller

#     elif guess < rannum:
#         print(f"Your guess {guess} is too small")
#     # equal
#     else:
#         print(f"{guess} is correct!")
#         break
# else:
#     print(f"You lost. The number was {rannum}")




# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Pass/Fail Checker
# Write a program to check if a student's score is a pass or 
# fail. Passing marks are 50 and above. Example: Input = 65.
# Output: "Pass."
# score = int(input("Enter score: "))
# if score >= 50:
#     print("pass")
# else:
#     print("fail")




#------------------------------------------------------------

# Exercise 9: Finding the Largest of Three Numbers
# Write a program to find the largest of three numbers.
# Example: Input = 4, 7, 2. Output = "The largest is 7."

# num1 = 350
# num2 = 32
# num3= 97
# if num1 > num2 and num1 > num3:
#     # print(num1)
#     print(f"{num1} is the biggest")
# elif num2 > num1 and num2 > num3:
#     # print(num2)
#     print(f"{num2} is the biggest")
# else:
#     # print(num3)
#     print(f"{num3} is the biggest")






#------------------------------------------------------------
# Exercise 10: Leap Year Checker
# Write a program to check if a year is a leap year.
# Example: Input = 2024. Output = "Leap year."






#------------------------------------------------------------
# Exercise 11: Age-Based Group Assignment
# Write a program to categorize a person into groups based 
# on age: Child (0-12), Teen (13-19), Adult (20+).
# Example: Input = 15. Output = "Teen."






#------------------------------------------------------------
# Exercise 12: Grade Checker
# Write a program to assign a grade based on marks:
# >= 90: A, >= 75: B, >= 60: C, < 60: D.
# Example: Input = 85. Output = "Grade B."

# Exercise 13: Even/Odd Checker
# Write a program to check if a number is even or odd.
# Example: Input = 4. Output = "Even number."





# Recap and Warm up - DO THIS

# write a program to help categorise how much bus fare to pay

# ask user to input an age

# check if age is a valid number # <str>.isdigit()

# use if, elif and else
# age < 7, free
# between 7 to 12, $2.00
# between 13 to 21, $4.00
# between 22 to 60, $10.00
# 61 and above, $1.00

# Print out the correct fare according to the age.

# age = int(input("Enter your age: "))
# if age < 7:
#     print("bus fare is free")
# elif age <= 12:
#     print("bus fare is $2.00")
# elif age <= 21:
#     print("bus fare is $4.00")
# elif age <= 60:
#     print("bus fare is $10.00")
# else:
#     print("bus fare is $1.00")