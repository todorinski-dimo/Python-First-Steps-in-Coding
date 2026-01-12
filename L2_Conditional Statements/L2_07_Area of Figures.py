from math import pi
figure = input()
area = 0
if figure == "square":
    side_sq = float(input())
    area = side_sq * side_sq
    print(f"{area:.03f}")
elif figure == "rectangle":
    side1_rc = float(input())
    side2_rc = float(input())
    area = side1_rc * side2_rc
    print(f"{area:.03f}")
elif figure == "triangle":
    side1_tr = float(input())
    side2_tr = float(input())
    area = (side1_tr * side2_tr) / 2
    print(f"{area:.03f}")
elif figure == "circle":
    side1_c = float(input())
    area = side1_c * side1_c * pi
    print(f"{area:.03f}")