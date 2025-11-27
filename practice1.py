# A student is writing a program to note down 
# the favourite sports of each of his classmates.
# the program will help check how many students like a certain sport.



# Write a program that will 
# -------------------------------------------------
# 1. ask how many students there are in the class

# num_students = int(input("Enter the number of students in the class: "))
# # -------------------------------------------------
# # 2. for each student, ask what is their favourite sport
# 	# 2a. Add the sport into a list

# sportlist = []
# # 2. for each student, ask what is their favourite sport
# for student in range(num_students):
#     sport = input("What is your favourite sport? ")
#     # 2a. Add the sport into a list
#     sportlist.append(sport)
# print(sportlist) # testing
# # -------------------------------------------------
# # 3. After asking all the student's sport, 
# 	# Ask the user to enter a sport to check how many students like the sport.

# check_sport = input("What sport do you want to check? ")
# counter = 0
# # -------------------------------------------------
# # 4. if the sport exist, print out how many people like the sport.
# 	# e.g. # 3 students like the sport

# # existance check
# if check_sport in sportlist:
#     # count how many people like it
#     for sport in sportlist:
#         if check_sport == sport:
#             counter = counter + 1
#     print(f"{counter} students like {check_sport}")
# # -------------------------------------------------
# # 5. if the sport does not exist, print out an appropriate message.

# # ** Assume that all inputs given are in lower case and valid.
# # ** the program will work for any number of students.

# else:
#     print(f"Nobody likes {check_sport}")





















num_students = int(input("Enter the number of stuents: "))
sportlist = []
for i in num_students:
    sportlist.append(num_students)
check_sport = input("")