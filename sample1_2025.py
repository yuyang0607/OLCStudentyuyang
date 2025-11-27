# Task 2

# The following program allows the weights of 15 bags of rice to be input. 
# The correct weight for each bag of rice must be 
# between 4.9 kg and 5.1 kg inclusive.

bags_rice = 15
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")    

# 7       Edit the program so that it:
# a.       Accepts the weights for only 10 bags of rice.
# [1]

# b.       Prints out the message “The bag of rice is the correct weight” 
# when a weight entered is between 4.9kg and 5.1 kg inclusive.
# [2]

# c.       Prints out the number of bags of rice that were underweight, 
# as well as the number that were overweight, after the weights of all 
# the bags have been entered.
# [5]

# d. Edit your program so that it works for any number of bags of rice.
# [2]   # 4.5
# Save your program.

underweight_bags = 0 # 1
overweight_bags = 0 # 1
bags_rice = 10 # 1
upper_bound = 5.1
lower_bound = 4.9
for i in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        overweight_bags = overweight_bags + 1 # 1
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        underweight_bags = underweight_bags + 1 # 1
        print("The bag of rice is underweight")
    if bag_weight >= lower_bound <= upper_bound:
        print("The bag of rice is the correct weight")
    break
print(f"there are {underweight_bags} bags that are underweight and {overweight_bags} that are overweight.")