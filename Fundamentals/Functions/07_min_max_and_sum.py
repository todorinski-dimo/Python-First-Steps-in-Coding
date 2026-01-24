input_list = input().split()
input_list = [int(item) for item in input_list]

min_number = min(input_list)
max_number = max(input_list)
sum_number = sum(input_list)

print(f"The minimum number is {min_number}")
print(f"The maximum number is {max_number}")
print(f"The sum number is: {sum_number}")
