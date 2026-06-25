def print_print(size:int, i:int) -> None:
        print(" " * (size - i) + "* " * i)

def print_lines_upper(size:int) -> None:
    for i in range(1, size):
        print_print(size, i)

def print_lines_lower(size:int) -> None:
    for i in range(size, 0, -1):
        print_print(size, i)

def print_rhombus(size:int) -> None:
    print_lines_upper(size)
    print_lines_lower(size)

n = int(input())
print_rhombus(n)