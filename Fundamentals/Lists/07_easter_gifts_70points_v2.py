"A little bit more straight forward option for code, but with same defect."

#Variable of type list is created and assigned an input string, split by space.
gifts_list = input().split()

#Commands and data changes are organised in a "while" cycle with a specific exit @ "No Money" command.
while True:
    cmd = input()
    
"""Before transforimg the command input in list with space separator, 
it is been checked for the cycle "exit" command (as it also has space in it)."""
    if cmd == "No Money":
        break
        
""" If command is not the exit one, command is split in list with space as separator. 
It can not have ["No", "Money"] in the command list as cycle breaks and new command is expected as unput"""
    cmd = cmd.split()

"""Command list first([0]) entry is checked for predefined commands.
Command second([1]) entry is the new gift name."""
    if cmd[0] == "OutOfStock":

"""When command is "OutOfStock" it iterates through the initial list with gifts and changes the entry
to the specified "None" one. It goes from 0 to the "len of list with gifts" (excluding it). 
So if there are 8 gifts, we go from 0 to 7, which checks all 8 entries."""
        for gift_pos in range(len(gifts_list)):
            if gifts_list[gift_pos] == cmd[1]:
                gifts_list[gift_pos] = "None"
                
"""When command is "Required" input has third entry(in the list) as a specific index.
Specific index is checked if exists (again it can only be nuber lower the the number of entries in the gifts list).
If so, the etry in gifts list is changed from the one in command."""
    elif cmd[0] == "Required":
        if int(cmd[2]) < len(gifts_list):
            gifts_list[int(cmd[2])] = cmd[1]

"""When command is "JustInCase", we find the index of the last entry in the gifts list and change it with
the on in the command"""
    elif cmd[0] == "JustInCase":
        gifts_list[-1] = cmd[1]

"""This time no records from the gifts list is removed, records "None" are skipped when printing the last result. 
Space is not put after the last gift record is printed."""
for gift_pos in range(len(gifts_list)):
    if gifts_list[gift_pos] != "None":
        print(f"{gifts_list[gift_pos]}", end="")
        if gift_pos < len(gifts_list) - 1:
            print(" ", end="")
