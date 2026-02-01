needed_love = [int(item) for item in input().split("@")]
pos = 0
need_love = 0

while True:
    cmd = input().split()
    if cmd[0] == "Love!":
        break
    if cmd[0] == "Jump":
        pos += int(cmd[1])
        if pos >= len(needed_love):
            pos = 0
        if needed_love[pos] == 0:
            print(f"Place {pos} already had Valentine's day.")
            continue
        needed_love[pos] -= 2
        if needed_love[pos] == 0:
            print(f"Place {pos} has Valentine's day.")

print(f"Cupid's last position was {pos}.")
for index in range(len(needed_love)):
    if needed_love[index] > 0:
        need_love += 1
if need_love > 0:
    print(f"Cupid has failed {need_love} places.")
else:
    print("Mission was successful.")