#Using diff loops to identify(count) 0, remove 0 and add 0 at the back
found_zeros = 0
input_list = input().split(", ")
input_list = [int(item) for item in input_list]

for item in range(len(input_list)):
    if input_list[item] == 0:
        found_zeros += 1

for item in range(found_zeros):
    input_list.remove(0)

for item in range(found_zeros):
    input_list.append(0)
print(input_list)
