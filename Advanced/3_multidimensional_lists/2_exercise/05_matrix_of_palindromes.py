rows, cols = map(int, input().split())
starting_char = ord("a")

matrix = [[f"{chr(starting_char+row)}{chr(starting_char+row+col)}{chr(starting_char+row)}" for col in range(cols)] for row in range(rows)]

[print(" ".join(row)) for row in matrix]

