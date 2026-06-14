TEE_TARGET = 10
n = int(input())

matrix = []
alice = []
tee_bags = 0

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice = [row, col]

possible_moves = {
    "down": (1, 0),
    "right": (0, 1),
    "up": (-1, 0),
    "left": (0, -1),
}

while tee_bags < TEE_TARGET:
    move = input()
    step = possible_moves[move]
    row = alice[0] + step[0]
    col = alice[1] + step[1]
    if row < 0 or row >= n or col < 0 or col >= n:
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    if matrix[row][col] not in ".*":
        tee_bags += int(matrix[row][col])

    matrix[row][col] = "*"
    alice = [row, col]

if tee_bags < TEE_TARGET:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(" ".join(row)) for row in matrix]
