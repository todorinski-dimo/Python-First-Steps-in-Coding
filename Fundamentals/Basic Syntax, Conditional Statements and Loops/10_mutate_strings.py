first_string = input()
second_string = input()
new_string = ""
for pos in range(len(first_string)):
    new_string = second_string[:pos + 1] + first_string[pos + 1:]
    if first_string[pos] != second_string[pos]:
        print(f"{new_string}")


