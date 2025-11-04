# This is a copy of the original code

#Task 3.1
# book_authors = {
#     'Winnie the pooh': 'A. A. Milne',
#     'The tale of peter rabbit': 'Beatrix Potter',
#     'The wind in the willows': 'Kenneth Grahame',
#     'The lion, the witch and the wardrobe': 'C. S. Lewis',
#     'Charlie and the chocolate factory': 'Roald Dahl'
# }

# book = input('Please enter the title of a book: ')
# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")
###############################################################################
# SLICING, slice up a word 
# WORD = "SINGAPORE"
# WORD[0] # 1st letter of the word
# WORD[-1] # last letter of the word
# # WORD[start: stop: step]
# WORD[:3] # return SIN
# WORD[3:6] # return GAP
# WORD[5:] # PORE
# WORD[-4:] # Always the last 4 characters

# Task 3.1
# Edit the program so that it converts the first letter of the first word of the 
# book title input for book to upper case.
# Save your program. [1]

# book_authors = {
#     'Winnie the pooh': 'A. A. Milne',
#     'The tale of peter rabbit': 'Beatrix Potter',
#     'The wind in the willows': 'Kenneth Grahame',
#     'The lion, the witch and the wardrobe': 'C. S. Lewis',
#     'Charlie and the chocolate factory': 'Roald Dahl'
# }

# book = input('Please enter the title of a book: ')
# book = book[0].upper() + book[1:]
# print(book)
# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")
###############################################################################################################
# Task 3.2

# Copy and paste your program from sub-task 3.1.

# Edit your program so that it outputs the author of the book that is input. 
# A suitable output message must be used.

# Save your program. [2]

# book_authors = {
#     'Winnie the pooh': 'A. A. Milne',
#     'The tale of peter rabbit': 'Beatrix Potter',
#     'The wind in the willows': 'Kenneth Grahame',
#     'The lion, the witch and the wardrobe': 'C. S. Lewis',
#     'Charlie and the chocolate factory': 'Roald Dahl'
# }

# title = "the diary of a lion"
# book = input('Please enter the title of a book: ')
# book = book[0].upper() + book[1:]
# print(book)
# author = book_authors[book]
# print(author)
# add = input("Would you like to add a book> Y or N: ")
# amend = input("Would you like to change the author of a book? Y or N: ")

# Copy and paste your program from sub-task 3.2.

# Edit your program so that if the user enters the value 'Y' when the user is asked about adding a book, it:

# asks the user for the title of the book to be added
# takes the title of the book as input
# asks the user for the author of the book to be added
# takes the author of the book as input
# adds the title and its author to the dictionary in the format title:author
# outputs the dictionary at the end of the program.
# You do not need to consider any validation for the input of the book title and the author. 
# You do not need to convert the first letter of the first word of the book title to upper case.

# Save your program. [4]
###############################################################################################################
# This is a backup of a buggy programme

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
rejected = 0 #1.change 100 to 0
rider = 0
age = int(input("Please enter your age ")) #2.add "
height = float(input("Please enter your height ")) 
while age > 0 and height != 0: #3.change <> to >
    if age <= 7: #4.change < to <=
        print("You are too young to ride") 
    elif age > 70: #5. change 90 to 70 #6.change if to elif
        print("You are too old to ride") 
    elif height <= 1.3: #7.change if to elif
        print("You are too short to ride") 
    rejected = rejected + 1 #8.change - to +
else:
    if age < 7 and age > 70 and height <= 1.3: #9.move orginal line 118 to line 126 #10.change or to and
        print("You can ride the Roller Coaster") 
    rider = rider + 1 #11.change Rider to rider
age = int(input("Please enter your age "))
height = float(input("Please enter your height ")) 
print("Number of people rejected ", rider) 
print("Number of riders ", rejected)