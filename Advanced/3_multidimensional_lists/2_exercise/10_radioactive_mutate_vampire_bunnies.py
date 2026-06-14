def explode_bunnies(mtrx, str_bun):
    new_bunnies = set()
    expld = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for b_row, b_col in str_bun:
        for e_row, e_col in expld:
            new_row, new_col = e_row + b_row, e_col + b_col
            if 0 <= new_row < len(mtrx) and 0 <= new_col < len(mtrx[0]):
                mtrx[new_row][new_col] = "B"
                new_bunnies.add((new_row, new_col))
    return mtrx, str_bun.union(new_bunnies)


rows, cols = map(int, input().split())
matrix = []
player_row = 0
player_col = 0
bunnies = set()
win = False

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col
        elif matrix[row][col] == 'B':
            bunnies.add((row, col))


commands = list(input())

command_map = {
    "U": lambda r, c: (r-1, c),
    "D": lambda r, c: (r+1, c),
    "L": lambda r, c: (r, c-1),
    "R": lambda r, c: (r, c+1)
}

for command in commands:
    new_p_row, new_p_col = command_map[command](player_row, player_col)
    matrix, bunnies = explode_bunnies(matrix, bunnies)

    if (player_row, player_col) not in bunnies:
        matrix[player_row][player_col] = "."

    if new_p_row < 0 or new_p_row >= rows or new_p_col < 0 or new_p_col >= cols:
        win = True
        break

    player_row, player_col = new_p_row, new_p_col
    if matrix[player_row][player_col] == "B":
        break

for row in matrix:
    print("".join(row))

if win:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")
