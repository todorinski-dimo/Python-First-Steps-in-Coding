input_string = input()
buff = ""
cmd = input().split(" ")

while cmd[0] != "Finalize":
    if cmd[0] == "Encrypt":
        input_string = input_string[::-1]
        print(input_string)
    elif cmd[0] == "Decrypt":
        for char in input_string:
            if char.islower():
                buff += char.upper()
            else:
                buff += char.lower()
        input_string = buff
        print(input_string)
    elif cmd[0] == "Substitute":
        if cmd[1] in input_string:
            input_string = input_string.replace(cmd[1], cmd[2])
            print(input_string)
        else:
            print("Character not found.")
    elif cmd[0] == "Scramble":
        if int(cmd[1]) >= len(input_string):
            print("Index out of bounds.")
        else:
            first = input_string[:int(cmd[1])]
            second = input_string[int(cmd[1]) + 1:]
            input_string = first + cmd[2] + second
            print(input_string)
    elif cmd[0] == "Remove":
        input_string = input_string.replace(cmd[1], "")
        print(input_string)
    else:
        print("Invalid command detected!")
    buff = ""
    cmd = input().split(" ")
