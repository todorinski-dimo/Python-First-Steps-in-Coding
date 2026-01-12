number = int(input())
list_number = list(str(number))
list_number.sort()
new_number = 0
for pos in range(len(list_number)):
    new_number += (10 ** pos) * int(list_number[pos])
print(new_number)