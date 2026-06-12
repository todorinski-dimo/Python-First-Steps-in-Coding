def print_triangle_part_one(num):
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(col, end=" ")
        print()


def print_triangle_part_two(num):
    for row in range(1, num):
        for col in range(1, num - row + 1):
            print(col, end=" ")
        print()

def print_triangle(num):
    print_triangle_part_one(num)
    print_triangle_part_two(num)