input_string = input()
input_string_list = list(input_string)
new_list = []
for pos in range(len(input_string_list)):
    if 65 <= ord(input_string_list[pos]) <= 90:
        new_list.append(pos)
print(new_list)
