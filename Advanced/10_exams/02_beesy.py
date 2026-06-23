n = int(input())
matrix = []
bee = []
energy = 15
nectar = 0
restored_energy = False
for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'B':
            bee.append(row)
            bee.append(col)

commands_map = {
    "up": lambda r, c: ((r-1) % n, c % n),
    "down": lambda r, c: ((r+1) % n, c % n),
    "left": lambda r, c: (r % n, (c-1) % n),
    "right": lambda r, c: (r % n, (c+1) % n)
}
matrix[bee[0]][bee[1]] = "-"
while True:
    command = input()
    bee = commands_map[command](bee[0], bee[1])
    energy -= 1
    pos = matrix[bee[0]][bee[1]]
    if pos.isdigit():
        nectar += int(pos)
        matrix[bee[0]][bee[1]] = "-"
    elif pos == "H" and nectar >= 30:
        print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        break
    elif pos == "H" and nectar < 30:
        print("Beesy did not manage to collect enough nectar.")
        break
    if energy <= 0 and nectar >= 30 and not restored_energy:
        restored_energy = True
        energy += nectar - 30
        nectar = 30
    elif energy <= 0 and nectar >= 30 and restored_energy:
        print(f"This is the end! Beesy ran out of energy.")
        break
    elif energy <= 0 and nectar < 30:
        print(f"This is the end! Beesy ran out of energy.")
        break

matrix[bee[0]][bee[1]] = "B"
for row in matrix:
    print(*row, sep='')






