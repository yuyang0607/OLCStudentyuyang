# for loop generate number from 0 - 9
# for i in range(0, 10, 1):
#     print(i)

# for loop generate number from 15 - 24
# for i in range(15, 25, 1):
#     print(i)

# for loop through the following string value, and print out all characters
word = "SINGAPORE IS A HOT AND HUMID CITY IN ASIA"
A_count = 0
O_count = 0
for i in word:
    if i == "A":
        A_count = A_count + 1
        print(A_count)
    elif i == "O":
        O_count = O_count + 1
        print(O_count)