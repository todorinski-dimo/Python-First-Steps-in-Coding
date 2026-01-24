def is_palindrome(input_num: str) -> bool:
    if input_num == input_num[::-1]:
        return True
    return False


input_list = input().split(", ")
for item in input_list:
    print(is_palindrome(item))
