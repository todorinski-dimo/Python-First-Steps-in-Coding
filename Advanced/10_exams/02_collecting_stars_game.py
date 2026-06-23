n = int(input())
matrix = []
player = []

for row in range(n):
    matrix.append(list(input().split()))
    for col in range(n):
        if matrix[row][col] == 'P':
            player.append(row)
            player.append(col)

possible_moves = {
    "down": (1, 0),
    "right": (0, 1),
    "up": (-1, 0),
    "left": (0, -1),
}

GOAL = 10
stars = 2
matrix[player[0]][player[1]] = '.'

while True:
    command = input()
    n_row, n_col = player[0] + possible_moves[command][0], player[1] + possible_moves[command][1]
    if not(0<= n_row < n) or not(0<= n_col < n):
        player[0], player[1] = 0, 0
        if matrix[player[0]][player[1]] == '*':
            stars += 1
            matrix[player[0]][player[1]] = '.'
    elif matrix[n_row][n_col] == '*':
        matrix[n_row][n_col] = '.'
        stars += 1
        player[0], player[1] = n_row, n_col
    elif matrix[n_row][n_col] == '#':
        stars -= 1
        if stars == 0:
            print("Game over! You are out of any stars.")
            break
    elif matrix[n_row][n_col] == '.':
        player[0], player[1] = n_row, n_col
    elif not(0<= n_row < n) and not(0<= n_col < n):
        player[0], player[1] = 0, 0
        if matrix[player[0]][player[1]] == '*':
            stars += 1
            matrix[player[0]][player[1]] = '.'
    if stars == GOAL:
        print("You won! You have collected 10 stars.")
        break

matrix[player[0]][player[1]] = 'P'
print(f"Your final position is {player}")
for row in matrix:
    print(" ".join(row))

