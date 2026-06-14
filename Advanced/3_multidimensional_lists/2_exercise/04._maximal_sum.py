rows, cols = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum = -float("inf")
max_row = 0
max_col = 0

for row in range(rows - 2):
    for col in range(cols - 2):
        sum_33 = 0
        for r in range(row, row+3):
            # for c in range(col, col+3):
            #     sum_33 += matrix[r][c]
            sum_33 += sum(matrix[r][0+col : 3+col])
        if sum_33 > max_sum:
            max_sum = sum_33
            max_row = row
            max_col = col

print(f"Sum = {max_sum}")
for row in range(max_row, max_row+3):
    print(" ".join(map(str, matrix[row][max_col:max_col+3])))
