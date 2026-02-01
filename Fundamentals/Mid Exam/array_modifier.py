# https://alpha.judge.softuni.org/contests/02-programming-fundamentals-mid-exam/2474/practice

array_of_ints = [int(item) for item in input().split()]

while True:
    cmd = input().split()
    if cmd[0] == "end":
        break
    if cmd[0] == "swap":
        array_of_ints[int(cmd[1])], array_of_ints[int(cmd[2])] = array_of_ints[int(cmd[2])], array_of_ints[int(cmd[1])]
    if cmd[0] == "multiply":
        array_of_ints[int(cmd[1])] *= array_of_ints[int(cmd[2])]
    if cmd[0] == "decrease":
        for index in range(len(array_of_ints)):
            array_of_ints[index] -= 1

array_of_ints = [str(item) for item in array_of_ints]
print(", ".join(array_of_ints))

