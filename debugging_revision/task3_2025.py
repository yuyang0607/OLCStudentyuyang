# age = 0
# height = float(0) 
# rejected = 100
# rider = 0
# age = int(input("Please enter your age ))
# height = float(input("Please enter your height ")) 
# while age <> 0 and height != 0:
#     if age < 7 or age > 70 or height <= 1.3: 
#         if age < 7:
#             print("You are too young to ride") 
#         if age > 90:
#             print("You are too old to ride") 
#         if height <= 1.3:
#             print("You are too short to ride") 
#         rejected = rejected - 1
# else:
#         print("You can ride the Roller Coaster") 
#         rider = Rider + 1
#     age = int(input("Please enter your age "))
#     height = float(input("Please enter your height ")) 
# print("Number of people rejected ", rider) 
# print("Number of riders ", rejected)

age = 0
height = float(0) 
rejected = 100
rider = 0
age = int(input("Please enter your age ")) # 1. missing quotation mark
height = float(input("Please enter your height ")) 
while age == 0:
    height == 0:            # 2. Incorrect bracket
        if age < 7 or age > 70 or height <= 1.3: 
        elif age <= 7:
            print("You are too young to ride") 
        if age > 70:
            print("You are too old to ride") 
        if height <= 1.3:
            print("You are too short to ride") 
        rejected = rejected - 1
else:
    print("You can ride the Roller Coaster") 
    rider = rider + 1
    age = int(input("Please enter your age"))
    height = float(input("Please enter your height ")) 
print("Number of people rejected ", rider) 
print("Number of riders ", rejected)