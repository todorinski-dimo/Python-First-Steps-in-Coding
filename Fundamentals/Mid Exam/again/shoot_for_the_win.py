targets = [int(item) for item in input().split()]
shot_targets = 0

while True:
    cmd = input()
    if cmd == "End":
        targets = [str(item) for item in targets]
        print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")
        break
    idx = int(cmd)
    if 0 <= idx < len(targets) and targets[idx] != -1:
        shot_targets += 1
        buff = targets[idx]
        targets[idx] = -1
        for index in range(len(targets)):
            if targets[index] > buff and targets[index] != -1:
                targets[index] -= buff
            elif targets[index] <= buff and targets[index] != -1:
                targets[index] += buff
