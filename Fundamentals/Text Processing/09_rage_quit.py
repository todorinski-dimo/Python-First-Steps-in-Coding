input_string = input()
sub_string = ""
list_string = []
multiplyer = ""
list_multiplyer = []
output_string = ""

previous_was_char = False
previous_was_digit = False

for idx in range(len(input_string)):
    if not input_string[idx].isdigit():
        sub_string += input_string[idx]
        if previous_was_digit:
            list_multiplyer.append(int(multiplyer))
            multiplyer = ""
        previous_was_char = True
        previous_was_digit = False
    else:
        multiplyer += input_string[idx]
        if previous_was_char:
            list_string.append(sub_string.upper())
            sub_string = ""
        if idx == len(input_string) - 1:
            list_multiplyer.append(int(multiplyer))
            multiplyer = ""
        previous_was_char = False
        previous_was_digit = True

for idx in range(len(list_string)):
    output_string += list_string[idx] * list_multiplyer[idx]

print(f"Unique symbols used: {len(set(output_string))}")
print(output_string)
