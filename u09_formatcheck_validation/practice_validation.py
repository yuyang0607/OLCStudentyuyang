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

while True:
    age = int(input("Enter student's age: "))
    if age >= 7 and age <= 16:
        break
    else:
        print("Invalid age.")