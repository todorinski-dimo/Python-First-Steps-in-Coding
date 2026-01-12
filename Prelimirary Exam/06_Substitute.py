k = int(input())
l = int(input())
m = int(input())
n = int(input())

counter = 0

for i1 in range(k,9):
    for i2 in range(9,l-1,-1):
        for i3 in range(m,9):
            for i4 in range(9,n-1,-1):
                if i4 % 2 == 0:
                    continue
                elif i3 % 2 !=0:
                    continue
                elif i2 % 2 == 0:
                    continue
                elif i1 % 2 != 0:
                    continue
                else:
                    if i1 == i3 and i2 == i4:
                        print("Cannot change the same player.")
                    else:
                        print(f"{i1}{i2} - {i3}{i4}")
                        counter += 1
                if counter == 6:
                    quit()


