# Paper 2 - 2025 O Level Computing
# Question for Task 2

# Task 2.1 [3]

# word_list = ["apple", "window", "bend", "paper", "thought"]
# Extend the program to:
# - ask the user to input a new word
# - take the new word as input
# - convert the new word to lower case
# - store the new word at the end of the list in a new space

# You do not need to consider any validation for the new word.

# Save your program
# ----------------------------------------------

word_list = ["apple", "window", "bend", "paper", "thought"]
word = input("Enter a new word: ")
lower_case = word.lower()
word_list.append(lower_case)
# ----------------------------------------------
# Task 2.2 [4]

# Copy and paste your program from sub-task 2.1
# Extend your program to 
# - search the list to find words that have 5 or more letters
# - count and output the number of words that have five or more letters, with a suitable output message.

# Save your program 
# ----------------------------------------------

word_list = ["apple", "window", "bend", "paper", "thought"]
word = input("Enter a new word: ")
lower_case = word.lower()
word_list.append(lower_case)

count = 0
for word in word_list:
    print(word)
    if len(word) >= 5:
        count = count + 1
print(f"There are {count} words with 5 or more letters")
# ----------------------------------------------
# Task 2.3 [3]

# Copy and paste your program from sub-task 2.2

# Extend your program to :
# - search the list to find words that begin and end with the same letter
# - count and output the number of words that begin and end with the same letter, with a suitable output message.

# Save your program for Task 2
# ----------------------------------------------

#word = "apple"
#word[0] # retrieve first character
#word[-1] # retrieve last character

# if word[0] == word[-1]:

word_list = ["apple", "window", "bend", "paper", "thought"]
word = input("Enter a new word: ")
lower_case = word.lower()
word_list.append(lower_case)

count = 0
for word in word_list:
    print(word)
    if len(word) >= 5:
        count = count + 1
print(f"There are {count} words with 5 or more letters")

similar_count = 0
for word in word_list:
    if word[0] == word[-1]:
        similar_count = similar_count + 1
print(f"{similar_count} words begin and end with the same letter")