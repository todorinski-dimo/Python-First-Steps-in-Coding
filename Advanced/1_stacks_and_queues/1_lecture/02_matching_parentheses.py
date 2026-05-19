def expressions(e_input: str) -> str:
    """extracting each set of parentheses on new row of a given algebraic expression"""
    e_output_string = ""
    e_stack = []
    for i in range(len(e_input)):
        if e_input[i] == "(":
            e_stack.append(i)
        elif e_input[i] == ")" and len(e_stack) > 0:
            e_start_index = e_stack.pop()
            e_end_index = i + 1
            if len(e_output_string) != 0:
                e_output_string += "\n"
            e_output_string += e_input[e_start_index:e_end_index]
    return e_output_string

input_string = input()
output_string = expressions(input_string)
print(output_string)