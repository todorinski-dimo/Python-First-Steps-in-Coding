priority_list = [0] * 10

while True:
    cmd = input().split("-")
    if cmd[0] == "End":
        break
    else:
        priority_list.pop(int(cmd[0]) - 1)
        priority_list.insert(int(cmd[0]) - 1, cmd[1])

priority_list = [item for item in priority_list if item != 0]
print(priority_list)
