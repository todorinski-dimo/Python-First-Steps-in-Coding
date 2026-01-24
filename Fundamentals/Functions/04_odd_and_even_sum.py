def odd_even_sum(input_string: str) -> str:
    """takes a number as string; returns a message with the sums of the even and odd digits from the input"""
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for char in input_string:
        if int(char) % 2 == 0:
            sum_of_even_digits += int(char)
        else:
            sum_of_odd_digits += int(char)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


input_int_as_string = input()
print(odd_even_sum(input_int_as_string))
