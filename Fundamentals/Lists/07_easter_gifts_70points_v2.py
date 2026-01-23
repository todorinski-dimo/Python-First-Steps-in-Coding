gifts_list = input().split()

while True:
    cmd = input()
    if cmd == "No Money":
        break
    cmd = cmd.split()
    if cmd[0] == "OutOfStock":
        for gift_pos in range(len(gifts_list)):
            if gifts_list[gift_pos] == cmd[1]:
                gifts_list[gift_pos] = "None"

    elif cmd[0] == "Required":
        if int(cmd[2]) < len(gifts_list):
            gifts_list[int(cmd[2])] = cmd[1]

    elif cmd[0] == "JustInCase":
        gifts_list[-1] = cmd[1]

for gift_pos in range(len(gifts_list)):
    if gifts_list[gift_pos] != "None":
        print(f"{gifts_list[gift_pos]}", end="")
        if gift_pos < len(gifts_list) - 1:
            print(" ", end="")
