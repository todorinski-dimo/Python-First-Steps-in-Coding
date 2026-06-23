MET_RES = -5
MOVE_RES = -5
STAT_RES = 10
STARTING_SHIP_RES = 100

current_ship_res = STARTING_SHIP_RES
space = []
ship_row = 0
ship_col = 0
next_ship_row = 0
next_ship_col = 0

n = int(input())
for row in range(n):
    space.append(input().split())
    for col in range(n):
        if space[row][col] == "S":
            ship_row = row
            ship_col = col

possible_moves = {
    "down": (1, 0),
    "right": (0, 1),
    "up": (-1, 0),
    "left": (0, -1),
}
while True:
    move = input()
    step = possible_moves[move]
    next_ship_row = ship_row + step[0]
    next_ship_col = ship_col + step[1]
    if next_ship_row < 0 or next_ship_row > n-1 or next_ship_col < 0 or next_ship_col > n-1:
        space[ship_row][ship_col] = "S"
        print("Mission failed! The spaceship was lost in space.")
        break
    elif space[next_ship_row][next_ship_col] == ".":
        if space[ship_row][ship_col] != "R":
            space[ship_row][ship_col] = "."
        ship_row = next_ship_row
        ship_col = next_ship_col
        current_ship_res += MOVE_RES
    elif space[next_ship_row][next_ship_col] == "M":
        if space[ship_row][ship_col] != "R":
            space[ship_row][ship_col] = "."
        ship_row = next_ship_row
        ship_col = next_ship_col
        current_ship_res += MOVE_RES + MET_RES
    elif space[next_ship_row][next_ship_col] == "R":
        if space[ship_row][ship_col] != "R":
            space[ship_row][ship_col] = "."
        ship_row = next_ship_row
        ship_col = next_ship_col
        current_ship_res += MOVE_RES + STAT_RES
    elif space[next_ship_row][next_ship_col] == "P":
        if space[ship_row][ship_col] != "R":
            space[ship_row][ship_col] = "."
        ship_row = next_ship_row
        ship_col = next_ship_col
        current_ship_res += MOVE_RES
        print(f"Mission accomplished! The spaceship reached Planet B with {current_ship_res} resources left.")
        break
    if current_ship_res < 5:
        space[ship_row][ship_col] = "S"
        print("Mission failed! The spaceship was stranded in space.")
        break


for row in space:
    print(" ".join(row))