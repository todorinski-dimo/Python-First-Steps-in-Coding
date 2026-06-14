n = int(input())
commands = input().split()

matrix = []
total_coal = 0
coal = 0
minar_row, minar_col = 0, 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "c":
            total_coal += 1
        elif matrix[row][col] == "s":
            minar_row, minar_col = row, col

commands_map = {
    "up": lambda r, c: (r-1, c) if r-1 >= 0 else (r, c),
    "down": lambda r, c: (r+1, c) if r+1 < n else (r, c),
    "left": lambda r, c: (r, c-1) if c-1 >= 0 else (r, c),
    "right": lambda r, c: (r, c+1) if c+1 < n else (r, c)
}

for command in commands:
    minar_row, minar_col = commands_map[command](minar_row, minar_col)
    if matrix[minar_row][minar_col] == "e":
        print(f"Game over! ({minar_row}, {minar_col})")
        break
    elif matrix[minar_row][minar_col] == "c":
        coal += 1
        matrix[minar_row][minar_col] = "*"
        if coal == total_coal:
            print(f"You collected all coal! ({minar_row}, {minar_col})")
            break
else:
    print(f"{total_coal-coal} pieces of coal left. ({minar_row}, {minar_col})")
