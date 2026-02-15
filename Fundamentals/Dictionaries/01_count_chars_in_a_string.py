init_input = input()
init_input = [char for char in init_input if char != " "]

dictionary = {}

for char in init_input:
    if char in dictionary:
        dictionary[char] += 1
    else:
        dictionary[char] = 1

for key, value in dictionary.items():
    print(f"{key} -> {value}")
