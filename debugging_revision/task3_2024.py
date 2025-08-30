# The program: 
# takes as the length (longest side), width (second longest side) 
#  and depth (shortest side) of the parcel 
# calculates whether the parcel is large, medium, or small 
# outputs the size of the parcel. 

# The parcel is: 
# large – if the length, width and depth are all greater than 50. 
# medium – if the length and width are greater than 50, 
#  but the depth is 50 or less. 
# small – if either the length or the width is 50 or less.
#  

### This is a back up of the original buggy code.

# flag = False
# while flag:
# 	length = float(input("What is the length of the parcel?"))
# 	width = float(input("What is the width of the parcel?"))
# 	depth = float(input("What is the depth of the parcel?"))
# 	if length > 50 and length > 50 and depth > 50:
# 		parcel_size = "large"
# 	elif length > 50 and width > 50 or depth > 50:
# 		parce_size = "medium"
# 	elif:
# 		parcel_size = "small"
# 	more_parcel = input("Do you want to enter another parcel? Y or N") 
# 	if more_parcel = N:
# 		flag = True
		

flag = True #False # 3. Change flag to true to start while loop

while flag:
	length = float(input("What is the length of the parcel?"))
	width = float(input("What is the width of the parcel?"))
	depth = float(input("What is the depth of the parcel?"))
	if length > 50 and width > 50 and depth > 50: #6. should be width not length
		parcel_size = "large"
		print(parcel_size)
	elif length > 50 and width > 50 or depth <= 50: # 7. should be <= for depth
		parcel_size = "medium" #8 should be parcel_size
		print(parcel_size)
	else: #elif: # 1. change elif to else
		parcel_size = "small"
		print(parcel_size)
	
    # print(parcel_size) # testing only. to remove later
	more_parcel = input("Do you want to enter another parcel? Y or N") 
	if more_parcel == "N": # 2. should be double equal, #4 should be "N"
		flag = False # 5. change to false to exit loop
	
    # print(parcel_size) # testing only. to remove later
# 1 run the program to identify all the syntax errors