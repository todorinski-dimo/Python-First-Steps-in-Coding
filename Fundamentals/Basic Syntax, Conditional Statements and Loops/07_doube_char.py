input_string = ""
while True:
    input_string = input()
    if input_string == "End":
        break
    if input_string == "SoftUni":
        continue
    else:
        new_string = ""
        for pos in range(len(input_string)):
            new_string += input_string[pos:pos + 1] * 2
        print(new_string)
