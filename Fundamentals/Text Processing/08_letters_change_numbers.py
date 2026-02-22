input_list = input().split()
value = 0

for item in input_list:
    sub_value = 0
    first_char = item[0]
    last_char = item[-1]
    number = int(item[1:-1])
    if 97 <= ord(first_char) <= 122:
        sub_value = number * (ord(first_char) - 96)
    else:
        sub_value = number / (ord(first_char) - 64)
    if 97 <= ord(last_char) <= 122:
        sub_value = sub_value + (ord(last_char) - 96)
    else:
        sub_value = sub_value - (ord(last_char) - 64)
    value += sub_value

print(f"{value:.2f}")
