phonebook = {}

while True:
    cmd = input().split("-")
    if len(cmd) == 1:
        counter = int(cmd[0])
        break
    else:
        phonebook[cmd[0]] = cmd[1]

for _ in range(counter):
    check_name = input()
    if check_name in phonebook:
        print(f"{check_name} -> {phonebook[check_name]}")
    else:
        print(f"Contact {check_name} does not exist.")
