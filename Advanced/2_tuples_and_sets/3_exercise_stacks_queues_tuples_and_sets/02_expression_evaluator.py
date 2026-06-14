from collections import deque

expression = input().split()
numbers = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,}

for char in expression:
    if char not in "+-*/":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            numbers.appendleft(operations[char](first_number, second_number))

print(*numbers)
