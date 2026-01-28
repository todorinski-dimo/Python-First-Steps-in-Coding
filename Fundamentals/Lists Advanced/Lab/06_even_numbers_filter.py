input_numbers = list(map(int, input().split(", ")))
filtered_even_numbers = list(filter(lambda index: input_numbers[index] % 2 == 0, range(len(input_numbers))))
print(filtered_even_numbers)
