input_string = input()
input_list = input_string.split()
new_list = []

# new_list = [int(item) for item in input_list]
for item in range(0, len(input_list)):
    new_list.append(int(input_list[item]))
    new_list[item] *= -1

print(new_list)
