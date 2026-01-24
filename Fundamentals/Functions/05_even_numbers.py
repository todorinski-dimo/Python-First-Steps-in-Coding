def is_even(number: int) -> bool:
    """takes an integer; returns True if even, False if odd"""
    return number % 2 == 0


input_list = input().split()
input_list = [int(item) for item in input_list]

filtered_list = filter(is_even, input_list)
print(list(filtered_list))
