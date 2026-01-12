range_start = int(input())
range_end = int(input())

range_start_str = str(range_start)
range_end_str = str(range_end)

for num in range(range_start, range_end+1):
    num_string = str(num)
    barcode = 4
    for pos in range(4):
        if int(range_start_str[pos]) <= int(num_string[pos]) <= int(range_end_str[pos]):
            if int(num_string[pos]) % 2 != 0:
                barcode -= 1
        else:
            break
    if barcode == 0:
        print(num, end=" ")
