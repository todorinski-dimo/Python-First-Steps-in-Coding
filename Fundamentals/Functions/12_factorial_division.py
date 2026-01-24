def factorial(number: int) -> int:
    for num in range(1, number):
        number *= num
    return number


input_num_first = int(input())
input_num_second = int(input())
print(f"{factorial(input_num_first) / factorial(input_num_second):.2f}")
