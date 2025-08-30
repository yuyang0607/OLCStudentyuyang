# This is a back up of the buggy code

# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     else:
#         students = True

students = True #2. change False to True
while students == True:
    comp = int(input("Enter the Computing test score ")) #3. add int #4. add an additional bracket after adding int 
    math = int(input("Enter the Mathematics test score ")) #1. add " 
    joint_score = comp + math #7. change one of the word "comp" to "math"
    if comp >= 100 and math >= 100: #6. Add = after >
        print("Student is awarded a gold award")
    elif (comp >= 100 or math >= 100) and joint_score >= 180: #9. change and between comp and math to or #10. change or joint_score to and joint_score
        print("Student is awarded a silver award")
    elif comp >= 75 and math >=75: #8. change comp and math results to joint_score results
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ").upper()
    if more_scores == 'N': #5. change More_scores to more_scores
        students = False #11. Change True to False
    else:
        students = True