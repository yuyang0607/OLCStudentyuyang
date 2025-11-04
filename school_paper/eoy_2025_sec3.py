def get_largest(numlist):
    # numlist is a list variable
    # find the maximum number in this list

    maxnum = numlist[0] # assume the first number is the biggest

    # loop through every number in the list
    for i in numlist:
        if i > maxnum:
            maxnum = i
    
    return maxnum

nums = [2, 5, 5, 10, 40]
print(get_largest(nums))