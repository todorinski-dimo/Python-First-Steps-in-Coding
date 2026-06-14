rows, cols = map(int, input().split())
matrix = [[x for x in input().split()]for row in range(rows)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    if (len(command) != 5 or command[0] != "swap" or int(command[1]) >= rows or int(command[2]) >= cols
            or int(command[3]) >= rows or int(command[4]) >= cols):
        print("Invalid input!")
        continue
    else:
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = (
            matrix[int(command[3])][int(command[4])], matrix[int(command[1])][int(command[2])])
        [print(" ".join(row)) for row in matrix]
