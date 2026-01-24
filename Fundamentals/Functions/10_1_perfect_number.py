def is_perfect(number: int) -> bool:
    """takes a integer; returns True if number equals to the sum of its proper positive divisors."""
    check_number = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            check_number += divisor
    return number == check_number


input_number = int(input("Enter max range: "))
for i in range(1, input_number + 1):
    if is_perfect(i):
        print(f"{i} is perfect number!")
