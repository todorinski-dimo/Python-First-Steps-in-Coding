energy = int(input())
wins = 0

while True:
    cmd = input()
    if cmd == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break
    energy_needed = int(cmd)
    if energy < energy_needed:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break
    else:
        wins += 1
        energy -= energy_needed
    if wins % 3 == 0:
        energy += wins