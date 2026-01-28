input_numbers = list(map(int, input().split(", ")))
filtered_even_numbers = [index for index in range(0, len(input_numbers)) if input_numbers[index] % 2 == 0]
print(filtered_even_numbers)
