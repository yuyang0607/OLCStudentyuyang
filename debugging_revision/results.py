# This is a backup of the original code

# name_list = []
# mark_list = []
# dist_list = []
# pass_list = []
# fail_list = []
# count = 1

# flag = True
# while flag == False:
#     name = input('Enter student's name: ')
#     name_list += [name]
#     while True:
#         mark = int(input('Enter score of student: '))
#         if mark >= 0 or mark <= 100:
#             break
#         else:
#             print('Invalid mark!')
#         mark_list += [mark]
#     count += 1
#     if mark > 75:
#         dist_list += [name]
#     elif mark >= 50:
#         pass_list += [name]
#     else:
#         fail_list += (name)
#     more = int(input('Would you like to enter another score, Y or N?: '))
#     if more == 'N':
#         flag = False
# average = round(max(mark_list)/len(mark_list), 2)
# num_dist = len(dist_list)
# num_fail = len(fail_list)
# print("You entered " + count + " scores.")
# print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
# print("Average score is " + str(average))

#############################################################################

name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 0   #4. change 1 to 0

flag = True
while flag == True:     #5. change False to True
    name = input("Enter student's name: ")      #1. use " " instead of ' '
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 and mark <= 100:       #6. change or to and
            break
        else:
            print('Invalid mark!')
    mark_list += [mark]     #10. mark should be outside of while loop
    count += 1
    if mark >= 75:          #2. change > to >=
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name]         #3. change () to []
    more = input('Would you like to enter another score, Y or N?: ')   #7. remove int
    if more == 'N':
        flag = False
print(mark_list)
average = round(sum(mark_list)/len(mark_list), 2)   #8. change max to sum
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + str(count) + " scores.") #9. add str
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))