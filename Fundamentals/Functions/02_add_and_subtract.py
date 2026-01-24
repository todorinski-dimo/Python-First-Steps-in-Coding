def sum_numbers(integer_one: int, integer_two: int) -> int:
    """takes 2 integers; returns their sum"""
    return integer_one + integer_two


def subtract(integer_one: int, integer_two: int) -> int:
    """takes 2 integers; returns subtraction of first and second integer"""
    return integer_one - integer_two


def add_and_subtract(integer_one: int, integer_two: int, integer_three: int) -> int:
    """takes three integers; returns the subtraction of the sum of first two and the third"""
    sum_numbers(integer_one, integer_two)
    return subtract(sum_numbers(integer_one, integer_two), integer_three)


input_num_first = int(input())
input_num_second = int(input())
input_num_third = int(input())

print(add_and_subtract(input_num_first, input_num_second, input_num_third))
