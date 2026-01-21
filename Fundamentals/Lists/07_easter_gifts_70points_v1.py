list_of_gifts = input().split()

while True:
    index = 0
    command = input()
    if command == "No Money":
        break
    list_of_command = command.split()
    if list_of_command[0] == "OutOfStock":
        for index in range(0, len(list_of_gifts)):
            if list_of_gifts[index] == list_of_command[1]:
                list_of_gifts[index] = "None"
    elif list_of_command[0] == "Required":
        if int(list_of_command[2]) < len(list_of_gifts):
            list_of_gifts[int(list_of_command[2])] = list_of_command[1]
    elif list_of_command[0] == "JustInCase":
        index = len(list_of_gifts) - 1
        list_of_gifts[index] = list_of_command[1]

for _ in range(0, list_of_gifts.count("None")):
    list_of_gifts.remove("None")

final_result = " ".join(list_of_gifts)
print(final_result)
