energy = int(input())
wins = 0

while True:
    cmd = input()
    if cmd == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break
    elif energy - int(cmd) < 0:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    else:
        energy -= int(cmd)
        wins += 1
    if wins % 3 == 0:
        energy += wins
