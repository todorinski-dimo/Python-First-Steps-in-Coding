targets = [int(item) for item in input().split()]

while True:
    cmd = input().split()
    if cmd[0] == "End":
        targets = [str(item) for item in targets]
        print("|".join(targets))
        break
    elif cmd[0] == "Shoot":
        index = int(cmd[1])
        power = int(cmd[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)
    elif cmd[0] == "Add":
        index = int(cmd[1])
        value = int(cmd[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif cmd[0] == "Strike":
        index = int(cmd[1])
        radius = int(cmd[2])
        if 0 <= (index - radius) and (index + radius) < len(targets):
            for idx in range((index + radius), (index - radius) - 1, -1):
                targets.pop(idx)
        else:
            print("Strike missed!")
