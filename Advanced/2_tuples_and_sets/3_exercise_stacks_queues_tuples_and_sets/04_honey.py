from collections import deque

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else 0}

working_bees = deque(int(item) for item in input().split())
nectar = [int(item) for item in input().split()]
operands = deque(input().split())

honey = 0

while working_bees and nectar:
    if nectar[-1] >= working_bees[0]:
        honey += abs(operations[operands[0]](working_bees[0], nectar[-1]))
        working_bees.popleft()
        nectar.pop()
        operands.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
