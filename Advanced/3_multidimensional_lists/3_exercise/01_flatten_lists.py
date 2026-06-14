input_list = input().split("|")
matrix = []
for i in range(len(input_list) - 1, -1, -1):
    row = input_list[i].split()
    if row:
        matrix.append(row)
[print(*row, end=" ") for row in matrix]