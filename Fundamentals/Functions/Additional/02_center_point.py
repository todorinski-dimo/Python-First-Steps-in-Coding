from math import floor


def center_length(x: float, y: float) -> float:
    """takes 2 coordinates (or lenghts of catheti); returns distance from center (0,0) (or the hipothenuse)"""
    return (x ** 2 + y ** 2) ** 0.5


input_coord_x1 = float(input())
input_coord_y1 = float(input())
input_coord_x2 = float(input())
input_coord_y2 = float(input())

if center_length(input_coord_x1, input_coord_y1) <= center_length(input_coord_x2, input_coord_y2):
    print(f"({floor(input_coord_x1)}, {floor(input_coord_y1)})")
else:
    print(f"({floor(input_coord_x2)}, {floor(input_coord_y2)})")
