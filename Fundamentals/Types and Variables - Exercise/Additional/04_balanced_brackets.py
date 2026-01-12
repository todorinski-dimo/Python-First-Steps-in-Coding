input_lines = int(input())

flag = "UNOPENED"
result = "UNBALANCED"

for _ in range(input_lines):
    string = input()
    if string == "(" and flag == "UNOPENED":
        flag = "OPENED"
        result = "UNBALANCED"
    elif string == "(" and flag == "OPENED":
        result = "UNBALANCED"
        flag = "NO FIX"
    elif string == ")" and flag == "UNOPENED":
        result = "UNBALANCED"
        flag = "NO FIX"
    elif string == ")" and flag == "OPENED":
        result = "BALANCED"
        flag = "UNOPENED"

print(result)
