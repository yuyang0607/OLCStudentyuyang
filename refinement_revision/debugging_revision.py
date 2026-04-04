name_list = []
mark_list = []
dist_list = []
pass_list = []
fail_list = []
count = 1

flag = True
while flag == True: #3. change False to True
    name = input('Enter student"s name: ') #1. use "
    name_list += [name]
    while True:
        mark = int(input('Enter score of student: '))
        if mark >= 0 or mark <= 100:
            break
        else:
            print('Invalid mark!')
        mark_list += [mark]
    count += 1
    if mark >= 75: #4. change > to >=
        dist_list += [name]
    elif mark >= 50:
        pass_list += [name]
    else:
        fail_list += [name] #2. change () to []
    more = int(input('Would you like to enter another score, Y or N?: '))
    if more == 'N':
        flag = False
average = round(max(mark_list)/len(mark_list), 2) # I will fix this later
num_dist = len(dist_list)
num_fail = len(fail_list)
print("You entered " + count + " scores.")
print(str(num_dist) + " students score distinction and " + str(num_fail) + " students failed.")
print("Average score is " + str(average))