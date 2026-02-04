targets = [int(item) for item in input().split()]
count = 0
temp = 0

while True:
    cmd = input()
    if cmd == "End":
        targets = [str(item) for item in targets]
        print(f"Shot targets: {count} ->", " ".join(targets))
        break
    cmd = int(cmd)
    if 0 <= cmd < len(targets) and targets[cmd] != -1:
        temp = targets[cmd]
        targets[cmd] = -1
        count += 1
        # print(f"shot: {targets}")
        for idx in range(len(targets)):
            if targets[idx] != -1 and targets[idx] <= temp:
                targets[idx] += temp
            elif targets[idx] != -1 and targets[idx] > temp:
                targets[idx] -= temp
            # print(f"values change: {targets}")
