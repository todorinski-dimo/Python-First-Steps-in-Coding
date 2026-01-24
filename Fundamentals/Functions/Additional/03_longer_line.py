from math import floor


def line_length(x: float, y: float) -> float:
    """takes 2 coordinates (or length of catheti); returns distance from center (0,0) (or the hypotenuse)"""
    return (x ** 2 + y ** 2) ** 0.5


def centered_line_length(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Moves the center (0,0) of the cartesian coordinate system to the fist point of the line and calculates the
    new coordinates of the second point of the line; returns the length of the line (or the hypotenuse)
    :param x1: x coord of first point
    :param y1: y coord of first point
    :param x2: x coord of second point
    :param y2: y coord of second point
    :return: the length of the line (or the hypotenuse)
    """
    result_x = x2 - x1
    result_y = y2 - y1
    return line_length(result_x, result_y)


line1_coord_x1 = float(input())
line1_coord_y1 = float(input())
line1_coord_x2 = float(input())
line1_coord_y2 = float(input())
line2_coord_x1 = float(input())
line2_coord_y1 = float(input())
line2_coord_x2 = float(input())
line2_coord_y2 = float(input())

if centered_line_length(line1_coord_x1, line1_coord_y1, line1_coord_x2, line1_coord_y2) >= \
        centered_line_length(line2_coord_x1, line2_coord_y1, line2_coord_x2, line2_coord_y2):
    if line_length(line1_coord_x1, line1_coord_y1) <= line_length(line1_coord_x2, line1_coord_y2):
        print(f"({floor(line1_coord_x1)}, {floor(line1_coord_y1)})({floor(line1_coord_x2)}, {floor(line1_coord_y2)})")
    else:
        print(f"({floor(line1_coord_x2)}, {floor(line1_coord_y2)})({floor(line1_coord_x1)}, {floor(line1_coord_y1)})")
else:
    if line_length(line2_coord_x1, line2_coord_y1) <= line_length(line2_coord_x2, line2_coord_y2):
        print(f"({floor(line2_coord_x1)}, {floor(line2_coord_y1)})({floor(line2_coord_x2)}, {floor(line2_coord_y2)})")
    else:
        print(f"({floor(line2_coord_x2)}, {floor(line2_coord_y2)})({floor(line2_coord_x1)}, {floor(line2_coord_y1)})")
