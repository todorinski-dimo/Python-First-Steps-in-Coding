input_numbers = list(map(int, input().split(", ")))

positive = [str(item) for item in input_numbers if item >= 0]
negative = [str(item) for item in input_numbers if item < 0]
even = [str(item) for item in input_numbers if item % 2 == 0]
odd = [str(item) for item in input_numbers if item % 2 != 0]
print("Positive: ", end="")
print(", ".join(positive))
print("Negative: ", end="")
print(", ".join(negative))
print("Even: ", end="")
print(", ".join(even))
print("Odd: ", end="")
print(", ".join(odd))