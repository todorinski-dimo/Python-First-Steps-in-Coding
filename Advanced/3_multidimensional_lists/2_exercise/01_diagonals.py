square = int(input())
matrix = [[int(x) for x in input().split(",")] for _ in range(square)]

primary_diagonal = [matrix[i][i] for i in range(square)]
secondary_diagonal = [matrix[i][-1 - i] for i in range(square)]

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
