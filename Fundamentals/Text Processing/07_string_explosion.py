input_string = input()
output_string = ""

explode_strength = 0

for idx in range(len(input_string)):
    if explode_strength > 0 and input_string[idx] != ">":
        explode_strength -= 1
    elif input_string[idx] == ">":
        explode_strength += int(input_string[idx + 1])
        output_string += input_string[idx]
    else:
        output_string += input_string[idx]

print(output_string)
