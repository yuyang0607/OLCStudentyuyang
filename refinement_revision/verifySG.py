ID = ""
for i in range(2):
    ID = input("Enter ID: ")
    if ID[0] == "S":
        print("Welcome home!")
    else:
        print("Welcome to Singapore!")
      
######################################################################
# Task 2.1

ID = ""
for i in range(5):
    ID = input("Enter ID: ")
    if ID[0] == "S":
        print("Welcome home!")
    else:
        print("Welcome to Singapore!")
      
######################################################################
# Task 2.2

ID = ""
while True:
    if len(ID) != 9:
        print("ID must be 9 characters")
    else:
        break
    ID = input("Enter ID: ")
    if ID[0] == "S":
        print("Welcome home!")
    else:
        print("Welcome to Singapore!")
      