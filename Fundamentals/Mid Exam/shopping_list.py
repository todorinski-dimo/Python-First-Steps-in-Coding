shop_list = input().split("!")

while True:
    cmd = input()
    if cmd == "Go Shopping!":
        break
    cmd = cmd.split()
    if cmd[0] == "Urgent":
        if cmd[1] not in shop_list:
            shop_list.insert(0, cmd[1])
    if cmd[0] == "Unnecessary":
        if cmd[1] in shop_list:
            index = shop_list.index(cmd[1])
            shop_list.pop(index)
    if cmd[0] == "Correct":
        if cmd[1] in shop_list:
            index = shop_list.index(cmd[1])
            shop_list[index] = cmd[2]
    if cmd[0] == "Rearrange":
        if cmd[1] in shop_list:
            index = shop_list.index(cmd[1])
            shop_list.pop(index)
            shop_list.append(cmd[1])

print(", ".join(shop_list))
