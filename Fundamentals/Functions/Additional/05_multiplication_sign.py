def is_zero(int_list: list) -> bool:
    """takes a list of integers; returns True if it contains 0"""
    if 0 in int_list:
        return True
    return False


def is_negative(int_list: list) -> bool:
    """takes a list of integers; returns True if there are odd negative values(items) in list"""
    negatives = 0
    for item in int_list:
        if item < 0:
            negatives += 1
    if negatives % 2 == 0:
        return False
    return True


def multiplication_sign(int_list: list) -> str:
    """takes a list of integers; returns messages of what would be the sign of the result of multiplication of
     all values (items) in the list"""
    if is_zero(int_list):
        return "zero"
    if is_negative(int_list):
        return "negative"
    return "positive"


first_num = int(input())
second_num = int(input())
third_num = int(input())
list_num = [first_num, second_num, third_num]
print(multiplication_sign(list_num))
