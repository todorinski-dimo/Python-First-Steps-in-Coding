def is_zero(int_list: list) -> bool:
    if 0 in int_list:
        return True
    return False


def is_negative(int_list: list) -> bool:
    negatives = 0
    for item in int_list:
        if item < 0:
            negatives += 1
    if negatives % 2 == 0:
        return False
    return True


def multiplication_sign(int_list: list) -> str:
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
