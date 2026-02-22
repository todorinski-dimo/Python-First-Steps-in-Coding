input_string = input()
output_string = ""

for ch in input_string:
    output_string += chr(ord(ch) + 3)

print(output_string)
