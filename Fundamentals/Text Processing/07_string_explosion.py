input_string = input()
output_string = ""

explode_strength = 0
available_for_explode = 0
pass_explode_str = 0
positions_to_explode = 0
idx = 0
for _ in range(len(input_string)):
    if idx >= len(input_string):
        break
    if input_string[idx] != ">":
        output_string += input_string[idx]
        idx += 1
    else:
        output_string += input_string[idx]
        explode_strength = int(input_string[idx + 1]) + pass_explode_str
        if input_string[idx + 1:].find(">") > - 1:
            available_for_explode = input_string[idx + 1:].find(">")
        else:
            available_for_explode = len(input_string[idx + 1:-1])
        if available_for_explode >= explode_strength:
            positions_to_explode = explode_strength
            pass_explode_str = 0
        else:
            positions_to_explode = available_for_explode
            pass_explode_str = explode_strength - available_for_explode
        idx += 1 + positions_to_explode

print(output_string)
