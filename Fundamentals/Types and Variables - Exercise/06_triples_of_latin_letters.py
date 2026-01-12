limit = int(input())

for i in range(0, limit):
    for k in range(0, limit):
        for j in range(0, limit):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")
