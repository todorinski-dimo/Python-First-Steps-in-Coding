input_string = input()
output_string = ""

for idx in range(len(input_string) - 1):
    if input_string[idx] != input_string[idx + 1]:
        output_string += input_string[idx]
    if idx == len(input_string) - 2:
        output_string += input_string[-1]

print(output_string)

