input_string = input()
output_list = []
for idx in range(len(input_string)):
    if input_string[idx] == ":" and idx + 1 < len(input_string):
        output_list.append(f"{input_string[idx]}{input_string[idx+1]}")
        idx += 1

for item in output_list:
    print(item)
