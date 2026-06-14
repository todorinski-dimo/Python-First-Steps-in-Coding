square = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(square)]

primary_diagonal = [matrix[i][i] for i in range(square)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(square)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
