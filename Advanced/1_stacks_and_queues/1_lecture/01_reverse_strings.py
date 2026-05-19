def reversal(r_input: str) -> str:
    """takes a sting, returns same string but reversed"""
    r_input_lst = list(r_input)
    r_output = ""
    for _ in range(len(r_input_lst)):
        r_output += r_input_lst.pop()
    return r_output

input_string = input()
output_string = reversal(input_string)
print(output_string)
