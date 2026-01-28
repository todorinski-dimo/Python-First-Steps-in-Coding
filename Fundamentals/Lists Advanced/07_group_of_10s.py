input_numbers = list(map(int, input().split(", ")))
group_list = []

group_max = 10
while len(input_numbers) > 0:
    for idx in range(len(input_numbers) - 1, -1, -1):
        if group_max - 10 < input_numbers[idx] <= group_max:
            group_list.append(input_numbers[idx])
            input_numbers.pop(idx)
        elif input_numbers == 0:
            input_numbers.pop(idx)
    group_list = group_list[::-1]
    print(f"Group of {group_max}'s: {group_list}")
    group_list = []
    group_max += 10
