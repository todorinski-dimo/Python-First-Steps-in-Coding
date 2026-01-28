courses_list = input().split(", ")

while True:
    cmd = input()
    if cmd == "course start":
        break
    cmd = cmd.split(":")
    if cmd[0] == "Add" and not courses_list.count(cmd[1]):
        courses_list.append(cmd[1])
    elif cmd[0] == "Insert" and not courses_list.count(cmd[1]):
        a = int(cmd[2])
        courses_list.insert(a, cmd[1])
    elif cmd[0] == "Remove" and courses_list.count(cmd[1]):
        a = courses_list.index(cmd[1])
        courses_list.remove(cmd[1])
        if courses_list.count(f"{cmd[1]}-Exercise") and courses_list.index(f"{cmd[1]}-Exercise") == a:
            courses_list.pop(a)
    elif cmd[0] == "Swap" and courses_list.count(cmd[1]) and courses_list.count(cmd[2]):
        a, b = courses_list.index(cmd[1]), courses_list.index(cmd[2])
        courses_list[a], courses_list[b] = courses_list[b], courses_list[a]
        if courses_list.count(f"{cmd[1]}-Exercise"):
            a = courses_list.index(f"{cmd[1]}-Exercise")
            courses_list.pop(a)
            b = courses_list.index(cmd[1])
            courses_list.insert(b + 1, f"{cmd[1]}-Exercise")
        if courses_list.count(f"{cmd[2]}-Exercise"):
            a = courses_list.index(f"{cmd[2]}-Exercise")
            courses_list.pop(a)
            b = courses_list.index(cmd[2])
            courses_list.insert(b + 1, f"{cmd[2]}-Exercise")
    elif cmd[0] == "Exercise" and courses_list.count(cmd[1]):
        courses_list.insert(courses_list.index(cmd[1]) + 1, f"{cmd[1]}-Exercise")
    elif cmd[0] == "Exercise" and not courses_list.count(cmd[1]):
        courses_list.append(cmd[1])
        courses_list.append(f"{cmd[1]}-Exercise")
    cmd.clear()

for item in courses_list:
    print(f"{courses_list.index(item) + 1}.{item}")

