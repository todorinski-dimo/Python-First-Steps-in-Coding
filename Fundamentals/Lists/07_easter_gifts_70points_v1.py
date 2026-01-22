#Variable of type list is created and assigned an input string, split by space.
list_of_gifts = input().split()

#Commands and data changes are organised in a "while" cycle with a specific exit @ "No Money" command.
while True:

""" Definition of "index" variable for iterating through the lists and 
nullifiying it every cycle may not be needed, but it is here for jusit in case. """
    index = 0
    command = input()

"""Before transforimg the command input in list with space separator, 
it is been checked for the cycle "exit" command (as it also has space in it)."""
    if command == "No Money":
        break
        
""" If command is not the exit one, command is split in list with space as separator. 
It can not have ["No", "Money"] in the command list as cycle breaks and new command is expected as unput"""
    list_of_command = command.split()

"""Command list first([0]) entry is checked for predefined commands.
Command second([1]) entry is the new gift name."""
    if list_of_command[0] == "OutOfStock":
        
"""When command is "OutOfStock" it iterates through the initial list with gifts and changes the entry
to the specified "None" one. It goes from 0 to the "len of list with gifts" (excluding it). 
So if there are 8 gifts, we go from 0 to 7, which checks all 8 entries."""
        for index in range(0, len(list_of_gifts)):
            if list_of_gifts[index] == list_of_command[1]:
                list_of_gifts[index] = "None"
                
"""When command is "Required" input has third entry(in the list) as a specific index.
Specific index is checked if exists (again it can only be nuber lower the the number of entries in the gifts list).
If so, the etry in gifts list is changed from the one in command."""
    elif list_of_command[0] == "Required":
        if int(list_of_command[2]) < len(list_of_gifts):
            list_of_gifts[int(list_of_command[2])] = list_of_command[1]
            
"""When command is "JustInCase", we find the index of the last entry in the gifts list and change it with
the on in the command"""
    elif list_of_command[0] == "JustInCase":
        index = len(list_of_gifts) - 1
        list_of_gifts[index] = list_of_command[1]

"""Finds out how much "None" entries are in the gifts list and removes of "None" entries from the gifts list.
It removes "None"s until there is no "None". When the last "None" is removed, range = (0,0) and the "remove"
method is not executed. This is done to prevent execptions."""
for _ in range(0, list_of_gifts.count("None")):
    list_of_gifts.remove("None")

"""All entries in the gift list are not concatenated in strin with space as separator"""
final_result = " ".join(list_of_gifts)

print(final_result)
