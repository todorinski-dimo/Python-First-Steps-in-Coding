inventory = [item for item in input().split(", ")]
combine = []
while True:
    cmd = input().split(" - ")
    if cmd[0] == "Craft!":
        break
    if cmd[0] == "Collect":
        if cmd[1] not in inventory:
            inventory.append(cmd[1])
    if cmd[0] == "Drop":
        if cmd[1] in inventory:
            inventory.remove(cmd[1])
    if cmd[0] == "Combine Items":
        combine = cmd[1].split(":")
        if combine[0] in inventory:
            index = inventory.index(combine[0])
            inventory.insert(index + 1, combine[1])
    if cmd[0] == "Renew":
        if cmd[1] in inventory:
            index = inventory.index(cmd[1])
            inventory.pop(index)
            inventory.append(cmd[1])

print(", ".join(inventory))
