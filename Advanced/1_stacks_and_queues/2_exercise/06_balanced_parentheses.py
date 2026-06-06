from fileinput import close

input_string = input()
buffer = []
mapper = {
    "(":")",
    "[":"]",
    "{":"}"
}

for char in input_string:
    if char in mapper.keys():
        buffer.append(char)
    elif char in mapper.values():
        if not buffer:
            print("NO")
            break
        last_opening = buffer.pop()
        if mapper[last_opening] != char:
            print("NO")
            break
else:
    if buffer:
        print("NO")
    else:
        print("YES")