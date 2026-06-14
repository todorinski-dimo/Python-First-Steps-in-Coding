SIZE = 5

matrix = []
player_row = 0
player_col = 0
targets = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            player_row = row
            player_col = col
        if matrix[row][col] == "x":
            targets += 1

possible_moves = {
    "down": (1, 0),
    "right": (0, 1),
    "up": (-1, 0),
    "left": (0, -1),
}

shot_target = []

for _ in range(int(input())):
    action = input().split()
    if action[0] == "shoot":
        row = player_row + possible_moves[action[1]][0]
        col = player_col + possible_moves[action[1]][1]
        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == "x":
                shot_target.append([row, col])
                matrix[row][col] = "."
                targets -= 1
                break
            row += possible_moves[action[1]][0]
            col += possible_moves[action[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(shot_target)} targets hit.")
            break
    elif action[0] == "move":
        steps = int(action[2])
        row = player_row + possible_moves[action[1]][0] * steps
        col = player_col + possible_moves[action[1]][1] * steps
        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == ".":
            matrix[player_row][player_col] = "."
            matrix[row][col] = "A"
            player_row = row
            player_col = col

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

for target in shot_target:
    print(target)
