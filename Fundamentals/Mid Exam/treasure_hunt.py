# https://alpha.judge.softuni.org/contests/06-programming-fundamentals-mid-exam-retake/1773/practice#2
# score 100

treasure_chest = input().split("|")
position = 0
stolen_seq = []
stolen = []

while True:
    cmd = input().split()
    if cmd[0] == "Yohoho!":
        break
    if cmd[0] == "Loot":
        for idx in range(1, len(cmd)):
            if cmd[idx] not in treasure_chest:
                treasure_chest.insert(0, cmd[idx])
    if cmd[0] == "Drop" and -1 < int(cmd[1]) < len(treasure_chest):
        treasure_chest.append(treasure_chest[int(cmd[1])])
        treasure_chest.pop(int(cmd[1]))
    if cmd[0] == "Steal":
        if len(treasure_chest) - int(cmd[1]) <= 0 and len(treasure_chest) > 0:
            stolen_seq.extend(treasure_chest)
            stolen.extend(treasure_chest)
            treasure_chest.clear()
        else:
            position = len(treasure_chest) - int(cmd[1])
            stolen_seq = treasure_chest[position:]
            stolen.extend(treasure_chest[position:])
            treasure_chest = treasure_chest[:position]
        if len(stolen) > 0:
            print(", ".join(stolen_seq))
    stolen_seq.clear()

if len(treasure_chest) > 0:
    loot_in_value = [int(len(item)) for item in treasure_chest]
    loot_sum = sum(loot_in_value)
    average_gain = loot_sum/len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
