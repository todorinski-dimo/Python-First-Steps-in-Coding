array = [int(item) for item in input().split()]

while True:
    cmd = input().split()
    if cmd[0] == "end":
        break
    if cmd[0] == "swap":
        index1 = int(cmd[1])
        index2 = int(cmd[2])
        array[index1], array[index2] = array[index2], array[index1]

    if cmd[0] == "multiply":
        index1 = int(cmd[1])
        index2 = int(cmd[2])
        array[index1] *= array[index2]
    if cmd[0] == "decrease":
        for idx in range(len(array)):
            array[idx] -= 1

array = [str(item) for item in array]
print(", ".join(array))
