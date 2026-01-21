input_string = input()
beggars = int(input())

input_list = input_string.split(", ")
values_list = []
beggars_values = []

# new_list = [int(item) for item in input_list]
for item in range(0, len(input_list)):
    values_list.append(int(input_list[item]))
beggar = 0
while beggar < beggars:
    beggar_value = 0
    for value in range(beggar, len(values_list), beggars):
        beggar_value += values_list[value]
    beggars_values.append(beggar_value)
    beggar += 1
print(beggars_values)