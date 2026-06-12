from Advanced.topic_modules.lecture.math_operations.core import calculate

text = input().split()
num1 = int(text[0])
num2 = int(text[2])
sign = text[1]

print(calculate(num1, num2, sign))