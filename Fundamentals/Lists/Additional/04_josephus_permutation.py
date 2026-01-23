men = input().split()
men = [int(man) for man in men]
dead_men = []

skips = int(input())
pos = skips - 1

while True:
    #print(men)
    #print(pos)
    if len(men) == 0:
        break
    if pos >= len(men):
        pos %= len(men)
    dead_men.append(men[pos])
    men.pop(pos)
    pos += skips - 1

print("[", end="")
for pos in range(len(dead_men)):
    if pos < len(dead_men) - 1:
        print(f"{dead_men[pos]},", end="")
    else:
        print(f"{dead_men[pos]}", end="")
print("]", end="")

