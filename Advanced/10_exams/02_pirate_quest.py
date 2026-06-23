n = int(input())
matrix = []
ship = []
treasures = 0
DURABILITY = 100
c_durability = DURABILITY
used_charm = False

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == "S":
            ship.append(row)
            ship.append(col)
        if matrix[row][col] == "*":
            treasures += 1

commands_map = {
    "up": lambda r, c: ((r-1) % n, c % n),
    "down": lambda r, c: ((r+1) % n, c % n),
    "left": lambda r, c: (r % n, (c-1) % n),
    "right": lambda r, c: (r % n, (c+1) % n)
}

matrix[ship[0]][ship[1]] = "."

while treasures:
    command = input()
    if command == "stop":
        print("Retreat! Some treasures remain unclaimed.")
        break
    ship = commands_map[command](ship[0], ship[1])
    if matrix[ship[0]][ship[1]] == "*":
        treasures -= 1
        matrix[ship[0]][ship[1]] = "."
    elif matrix[ship[0]][ship[1]] == "C":
        if not used_charm:
            c_durability = min(c_durability + 25, DURABILITY)
            used_charm = True
        matrix[ship[0]][ship[1]] = "."
    elif matrix[ship[0]][ship[1]] == "M":
        c_durability -= 25
        matrix[ship[0]][ship[1]] = "."
    if c_durability <= 0:
        print(f"Shipwreck! Last known coordinates ({ship[0]}, {ship[1]})")
        break

matrix[ship[0]][ship[1]] = "S"

if not treasures:
    print("Yo-ho-ho! All treasure chests collected!")
print(f"Ship Durability: {c_durability}")
if treasures:
    print(f"Unclaimed chests: {treasures}")
for row in matrix:
    print("".join(row))



