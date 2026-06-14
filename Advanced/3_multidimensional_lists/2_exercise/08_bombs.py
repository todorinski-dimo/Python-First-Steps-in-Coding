def explode(row, col, mtrx):
    size = len(mtrx)
    explosions = []
    bomb_value = mtrx[row][col]
    if bomb_value <= 0:
        return mtrx
    else:
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                if 0 <= r < size and 0 <= c < size:
                    explosions.append((r, c))
        for el in explosions:
            if mtrx[el[0]][el[1]] > 0:
                mtrx[el[0]][el[1]] -= bomb_value
        return mtrx


n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]
bombs = [[int(el) for el in list(item) if el.isnumeric()] for item in input().split()]
alive_cells = 0
alive_cells_sum = 0

for coord in bombs:
    ex_row, ex_col = coord
    matrix = explode(ex_row, ex_col, matrix)

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            alive_cells += 1
            alive_cells_sum += matrix[r][c]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_cells_sum}")
[print(*row) for row in matrix]




