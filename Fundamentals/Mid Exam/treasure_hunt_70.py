# https://alpha.judge.softuni.org/contests/06-programming-fundamentals-mid-exam-retake/1773/practice#2
# score 70

treasure_chest = input().split("|")
stolen = []
while True:
    adding_loot = []
    cmd = input()
    if cmd == "Yohoho!":
        break
    cmd = cmd.split()
    if cmd[0] == "Loot":
        for item in range(1, len(cmd),):
            if cmd[item] not in treasure_chest:
                treasure_chest.insert(0, cmd[item])
    if cmd[0] == "Drop":
        if 0 < int(cmd[1]) < len(treasure_chest):
            treasure_chest.append(treasure_chest[int(cmd[1])])
            treasure_chest.pop(int(cmd[1]))
    if cmd[0] == "Steal":
        if int(cmd[1]) >= len(treasure_chest):
            stolen.extend(treasure_chest)
            treasure_chest = []
        else:
            pos = len(treasure_chest) - int(cmd[1])
            stolen.extend(treasure_chest[pos:])
            treasure_chest = treasure_chest[:pos]

if len(stolen) > 0:
    print(", ".join(stolen))
if len(treasure_chest) > 0:
    loot_in_value = [int(len(item)) for item in treasure_chest]
    loot_sum = sum(loot_in_value)
    average_gain = loot_sum/len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

