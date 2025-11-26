'''
Question 1 (Length Check):
Write the input entry and validation code for a program that
needs to accept a 4-digit OTP (One-Time Password)
The OTP must be exactly 4 digits long

If the input is invalid, your code should keep trying
by asking for the input to be entered again.

#########################################

Sample output

Enter OTP: 12
Invalid input. The OTP must be exactly 4 digits.

Enter OTP: 12345

Invalid input. The OTP must be exactly 4 digits

Enter OTP: 1234
OTP accepted

'''

# how to check for length

# pin = "1234567891011121314151617181920"
# print(len(pin))
# while True:
#     otp = input("Enter a 4 digit OTP ")
#     # validation both for length and for numbers
#     if not otp.isdigit():
#         print("OTP must be a number!")
#     elif len(otp) != 4:
#         print("OTP must be 4 digits!")
#     else:
#         print("OTP is valid.")
#         break

# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# - At least one uppercase letter.
# - At least one lowercase letter.
# - At least one digit.

# Example:
# Input: "Secure123"
# Output: "Valid password"

# Input: "password"
# Output: "Invalid password"

## Bonus: Print out which of the requirement failed.

#boolean flag
#loop through every single character

# while True:
#     hasUpper = False
#     hasLower = False
#     hasNumber = False
#     password = input("Enter your pasword: ")
#     for char in password:
#         if char.isupper():
#             hasUpper == True
#         elif char.islower():
#             hasLower == True
#         elif char.isdigit():
#             hasNumber == True
#         print(password)

# write a program to ask for a student age
# keep asking until the age is between 7 to 16

# while True:
#     age = int(input("Enter student's age: "))
#     if age >= 7 and age <= 16:
#         break
#     else:
#         print("Invalid age.")