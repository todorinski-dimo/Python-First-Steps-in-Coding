num_list = input().split()
num_list = [int(item) for item in num_list]

odds_list = []
even_list = []

for num in num_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odds_list.append(num)

# print(even_list)
# print(odds_list)

# print(num_list)
while True:
    cmd = input()
    if cmd == "end":
        break
    cmd = cmd.split()
    # print(cmd)
    # print(cmd[0])
    # print(cmd[1])
    if cmd[0] == "exchange":
        odds_list = []
        even_list = []
        if 0 <= int(cmd[1]) < len(num_list):
            list_a = num_list[:int(cmd[1]) + 1]
            list_b = num_list[int(cmd[1]) + 1:]
            num_list = list_b + list_a
        else:
            print("Invalid index")
        for num in num_list:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odds_list.append(num)
        # print(even_list)
        # print(odds_list)
    elif cmd[0] == "max":
        if cmd[1] == "odd" and odds_list:
            max_value = max(odds_list)
            # print(max_value)
            for idx in range(len(num_list) - 1, -1, -1):
                # print(idx)
                if num_list[idx] == max_value:
                    print(idx)
                    break
        elif cmd[1] == "even" and even_list:
            max_value = max(even_list)
            # print(max_value)
            for idx in range(len(num_list) - 1, -1, -1):
                # print(idx)
                if num_list[idx] == max_value:
                    print(idx)
                    break
        else:
            print("No matches")
    elif cmd[0] == "min":
        if cmd[1] == "odd" and odds_list:
            min_value = min(odds_list)
            # print(min_value)
            for idx in range(len(num_list) - 1, -1, -1):
                # print(idx)
                if num_list[idx] == min_value:
                    print(idx)
                    break
        elif cmd[1] == "even" and even_list:
            min_value = min(even_list)
            # print(min_value)
            for idx in range(len(num_list) - 1, -1, -1):
                # print(idx)
                if num_list[idx] == min_value:
                    print(idx)
                    break
        else:
            print("No matches")
    elif cmd[0] == "first":
        if int(cmd[1]) <= len(num_list):
            if cmd[2] == "odd":
                odds_list_first = odds_list[:int(cmd[1])]
                print(odds_list_first)
            elif cmd[2] == "even":
                even_list_first = even_list[:int(cmd[1])]
                print(even_list_first)
        else:
            print("Invalid count")
    elif cmd[0] == "last":
        if int(cmd[1]) <= len(num_list):
            if cmd[2] == "odd":
                odds_list_last = odds_list[len(odds_list) - int(cmd[1]):]
                print(odds_list_last)
            elif cmd[2] == "even":
                even_list_last = even_list[len(even_list) - int(cmd[1]):]
                print(even_list_last)
        else:
            print("Invalid count")

print(num_list)
