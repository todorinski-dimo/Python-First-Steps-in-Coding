TIME = 16
current_time = TIME
n, m = map(int, input().split(", "))
matrix = []
c_pos = []
for row in range(n):
    matrix.append(list(input()))
    for col in range(m):
        if matrix[row][col] == "C":
            c_pos.append(row)
            c_pos.append(col)

commands_map = {
    "up": lambda r, c: (r-1, c) if r-1 >= 0 else (r, c),
    "down": lambda r, c: (r+1, c) if r+1 < n else (r, c),
    "left": lambda r, c: (r, c-1) if c-1 >= 0 else (r, c),
    "right": lambda r, c: (r, c+1) if c+1 < m else (r, c)
}

# matrix[c_pos[0]][c_pos[1]] = "*"

while True:
    command = input()
    if command != "defuse":
        current_time -= 1
        c_pos[0], c_pos[1] = commands_map[command](c_pos[0], c_pos[1])

        if matrix[c_pos[0]][c_pos[1]] == "T":
            matrix[c_pos[0]][c_pos[1]] = "*"
            print("Terrorists win!")
            break
    else:
        if matrix[c_pos[0]][c_pos[1]] != "B":
            current_time -= 2
        else:
            current_time -= 4
            if current_time >= 0:
                matrix[c_pos[0]][c_pos[1]] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {current_time} second/s remaining.")
                break
            else:
                matrix[c_pos[0]][c_pos[1]] = "X"
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {abs(current_time)} second/s.")
                break
    if current_time == 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: {abs(current_time)} second/s.")
        break

for row in matrix:
    print("".join(row))