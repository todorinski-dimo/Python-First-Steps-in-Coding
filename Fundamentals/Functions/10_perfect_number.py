def is_perfect(number: int) -> bool:
    """takes a integer; returns True if number equals to the sum of its proper positive divisors."""
    check_number = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            check_number += divisor
    return number == check_number


input_number = int(input())
if is_perfect(input_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
