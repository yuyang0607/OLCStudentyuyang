# fobj = open('filename.txt', 'r')

# content = fobj.read()

# print(content)

# counta = 0
# for c in content:
#     if c.lower() == 'a':
#         counta = counta + 1
        
# print(f"There are {counta} A in the file")
# with open('filename.txt', 'r') as fobj:
#     content = fobj.read()

#     print(content)

# with open('filename.txt', 'r') as fobj
#     daylist = fobj.readlines()

#     for day in daylist:
#         print(day, end="")

# randy = random.choice(daylist)
# print(f"Random day: {randay}")

# planetslist = ["mercury\n", "venus\n", "earth\n", 
#               "saturn\n", "jupiter\n", "uranus\n", "mars\n"]
# with open("planets.txt", "w") as fobj:
#     fobj.writelines(planetslist)

# tasklist = []
# while True:
#     task = input("What do you have to do today? ")
#     tasklist.append(task + "\n")

#     proceed = input("Type N to stop").upper()
#     if proceed =="N":
#         with open('task.txt', 'a') as fobj:
#             fobj.writelines(tasklist)
#         break

# A text file shapes.txt stores a list of shapes with a comma between each value.  

# The current contents of shapes.txt are: 
# star,sphere,square,triangle 

# A text file colours.txt stores a list of colours with a comma between each value.  

# The current contents of colours.txt are: 
# red,yellow,green,blue 

# A program reads the data from each file and creates a dictionary of the values 
# so that each shape has an associated colour. 
# The first value in each file will be joined, for example, star and red. 

# The data is stored in a global dictionary with the identifier data_stored. 

# with open('filename.txt', 'r') as fileobj:
    # content = fileobj.read()

# print(content)