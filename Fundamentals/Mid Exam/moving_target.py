targets = [int(item) for item in input().split()]
idx = 0
power = 0
idx_start = 0
idx_end = 0
radius = 0

while True:
    cmd = input().split()
    if cmd[0] == "End":
        targets = [str(item) for item in targets]
        print("|".join(targets))
        break
    elif cmd[0] == "Shoot" and -1 < int(cmd[1]) < len(targets):
        idx = int(cmd[1])
        power = int(cmd[2])
        targets[idx] -= power
        if targets[idx] <= 0:
            targets.pop(idx)
    elif cmd[0] == "Add":
        idx = int(cmd[1])
        power = int(cmd[2])
        if -1 < idx < len(targets):
            targets.insert(idx, power)
        else:
            print("Invalid placement!")
    elif cmd[0] == "Strike":
        idx = int(cmd[1])
        radius = int(cmd[2])
        idx_start = idx - radius
        idx_end = idx + radius
        if -1 < idx_start < len(targets) and -1 < idx_end < len(targets):
            for i in range(idx_end, idx_start - 1, -1):
                targets.pop(i)
        else:
            print("Strike missed!")

