number = int(input())
dev = 3

if number == 2 or number == 3 or number == 5:
    print("True")
elif number % 2 == 0:
    print("False")
else:
    for dev in range(2, number // 2):
        if number % dev == 0:
            print("False")
            break
    else:
        print("True")
