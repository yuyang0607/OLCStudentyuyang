bags_rice = 10
upper_bound = 5.1
lower_bound = 4.9
num_overwight = 0
num_underwight = 0
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight < lower_bound:
        print("bags of rice are underwight")
        num_underwight = num_underwight + 1 
    elif bag_weight > upper_bound:
        print("bags of rice are overweight")
        num_overwight = num_overwight + 1
    else:
        print("bags are the correct weight")
print(f"{num_underwight} is the number of bags that are underweight.") 
print(f"{num_overwight} is the number of bags that are overweight")