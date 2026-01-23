line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

matrix = []
matrix.append(line_1)
matrix.append(line_2)
matrix.append(line_3)

if matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2]:
    if matrix[0][0] == "1":
        print("First player won")
    elif matrix[0][0] == "2":
        print("Second player won")
    else:
        print("Draw!")
elif matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]:
    if matrix[0][0] == "1":
        print("First player won")
    elif matrix[0][0] == "2":
        print("Second player won")
    else:
        print("Draw!")
elif matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2]:
    if matrix[1][0] == "1":
        print("First player won")
    elif matrix[1][0] == "2":
        print("Second player won")
    else:
        print("Draw!")
elif matrix[2][0] == matrix[1][1] and matrix[2][0] == matrix[0][2]:
    if matrix[2][0] == "1":
        print("First player won")
    elif matrix[2][0] == "2":
        print("Second player won")
    else:
        print("Draw!")
elif matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]:
    if matrix[2][0] == "1":
        print("First player won")
    elif matrix[2][0] == "2":
        print("Second player won")
    else:
        print("Draw!")
elif matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0]:
    if matrix[0][0] == "1":
        print("First player won")
    elif matrix[0][0] == "2":
        print("Second player won")
    else:
        print("Draw!")
elif matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]:
    if matrix[0][1] == "1":
        print("First player won")
    elif matrix[0][1] == "2":
        print("Second player won")
    else:
        print("Draw!")
elif matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2]:
    if matrix[0][2] == "1":
        print("First player won")
    elif matrix[0][2] == "2":
        print("Second player won")
    else:
        print("Draw!")
else:
    print("Draw!")






