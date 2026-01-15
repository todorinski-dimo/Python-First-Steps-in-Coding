range_start = int(input())
range_end = int(input())


for num in range(range_start, range_end+1):
    num_string = str(num)
    even = 4
    for pos in range(4):
        if int(num_string[pos]) % 2 != 0:
            even -= 1
    if even == 0:
        print(num, end=" ")
