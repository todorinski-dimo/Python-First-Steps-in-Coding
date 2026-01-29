int_list = list(map(int, input().split()))
total = 0
while len(int_list) > 0:
    index = int(input())
    if index < 0:
        a = int_list[0]
        int_list[0] = int_list[-1]
        total += a
        for i in range(len(int_list)):
            if a >= int_list[i]:
                int_list[i] += a
            else:
                int_list[i] -= a
    elif index >= len(int_list):
        a = int_list[-1]
        int_list[-1] = int_list[0]
        total += a
        for i in range(len(int_list)):
            if a >= int_list[i]:
                int_list[i] += a
            else:
                int_list[i] -= a
    else:
        a = int_list[index]
        total += a
        for i in range(len(int_list)):
            if a >= int_list[i]:
                int_list[i] += a
            else:
                int_list[i] -= a
        int_list.pop(index)

print(total)
