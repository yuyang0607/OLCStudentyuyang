# This is a backup of the buggy programme

# colour_list = ['red','green', 'blue','orange', 'purple','yellow']
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_to_find)
# item_number = 0
# colour_found = False
# while colour_found == True:
#     while item_number > items:
#         if colour_list[item_number] = colour_to_find
#             print("There are " + str(item) + " colours in the list, " + colour_to_find + " is item " + str(iten_number - 1) + " in the list.")
#             colour_found = True
#             item_number = item_number
#         elif item_number == items - 1:
#             print("The colour is not in the list. ")
#             colour_found = False
#             item_number = items
#         else:
#             item_number = items

colour_list = ['red','green', 'blue','orange', 'purple','yellow']
colour_to_find = input("Which colour would you like to search for? ")
items = len(colour_list) #6. change to colour_list
item_number = 0
colour_found = False #7. set boolean to False first to start the loop
while colour_found == True: 
    while item_number > items: #8. should be less than items
        if colour_list[item_number] == colour_to_find: #1.change = to == #10. missing colon
            print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + int(item_number + 1) + " in the list.") #2.change str to int     #3.change iten_number to item_number     #4. change item to items #11. Change - to +
            colour_found = True
            item_number = items #9. change item_number to items
        elif item_number == items - 1:
            print("The colour is not in the list. ")
            item_number = items
        else:
            item_number = items #12. increment the value of item_number            
            colour_found = False #5.change colour_found = False in line 35 to line 38(now is line 37, because delete line 35)