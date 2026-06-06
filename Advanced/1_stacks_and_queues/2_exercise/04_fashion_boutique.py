clothes = [int(item) for item in input().split()]
rack_capacity = int(input())
racks = 0
buffer = 0
rack = 0
while len(clothes) != 0:
    buffer = clothes.pop()
    rack += buffer
    if rack > rack_capacity:
        clothes.append(buffer)
        racks += 1
        rack = 0
    if len(clothes) == 0 and rack > 0:
        racks += 1
print(racks)
