input_string = input().split()
new_string = [word * len(word) for word in input_string]
print("".join(new_string))