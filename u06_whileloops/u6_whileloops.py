# use the while loop and print out numbers from 0 to 5

# use the while loop and print out numbers from 1 to 5

# use the while loop and print out multiples of 5 from 5 to 50

# use the while loop and print out numbers from 10 to 1

# count = 0
# while count < 6:
#     print(count)
#     count = count + 1

# count = 1
# while count < 6:
#     print(count)
#     count = count + 1

# count = 5
# while count < 51:
#     print(count)
#     count = count + 5

# count = 10
# while count < 11:
#     print(count)
#     count = count - 1
#     if count == 0:
#         break










############################################
# Write a program to help sort students to primary, secondary and JC

# while loop validation

### check for number.isdigit()
while True: #infinite loop
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        if age > 16:
            print("You go to JC.")
        elif age > 12:
            print("You go to Secondary.")
        elif age > 6:
            print("You go to Primary.")
        else:
            print("You are too young.")
        break # complete this program
    else:
        print("this is not a number") # testing














###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Multiplication Table with While Loop
# Write a program to print the multiplication table of 7 up to 10.
# Example: 7 x 1 = 7, ..., 7 x 10 = 70.

# count = 1
# number = 7
# while count <= 10:
#     answer = 7 * count
    
#     print(f"{number} × {count} = {answer}")
    
#     count = count + 1

# num1 = 10
# num2 = 20

# check if num1 is bigger than num2
# if num1 > num2 == True:
#     print("num1 is greater than num2")

# Test 1:  print the numbers from 6 to 13

# count = 6
# while count <= 13:
#     print(count)
#     count = count + 1
# Test 2: print multiples of 2 from 2 to 24

# count = 2
# while count <= 24:
#     print(count)
#     count = count + 2

# count = 1
# while count <= 10:
#     print(count)
#     count = count + 1
#------------------------------------------------------------
# Exercise 8: Sum of Even Numbers
# Write a program to calculate the sum of even numbers between 1 
# and 20 using a while loop. Example: Output = 110.
 
# count = 1
# totalsum = 0
# while count <= 20:
    
#     print(count)
#     if count % 2 == 0: # even number or not
#         totalsum = totalsum + count

#     count = count + 1

# print(totalsum)
#------------------------------------------------------------
# Exercise 9: Guessing Game
# Write a program where the user has to guess a random number 
# between 1 and 10. Keep prompting until they guess correct number

# random_num = int(input("Enter a number from 1 to 10: "))
# for i in random_num(11):
#       print(i)
#------------------------------------------------------------
# Exercise 10: Input Validation for a Password
# Write a program that keeps asking the user to enter a password.
# If the password is correct, print "Access granted."

#password = input("Enter your password: ")
#while True:
#    print("Access granted.")
#    break
#else:
#	continue