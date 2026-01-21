cells = input().split("#")
water = int(input())
fire = 0
for cell in range(0, len(cells)):
    cells[cell] = cells[cell].split(" = ")

for_removal = []

for list_pos in range(0, len(cells)):
    if cells[list_pos][0] == "High":
        if 81 <= int(cells[list_pos][1]) <= 125:
            if water >= int(cells[list_pos][1]):
                water -= int(cells[list_pos][1])
                fire += int(cells[list_pos][1])
            else:
                for_removal.append(list_pos)
        else:
            for_removal.append(list_pos)
    elif cells[list_pos][0] == "Medium":
        if 51 <= int(cells[list_pos][1]) <= 80:
            if water >= int(cells[list_pos][1]):
                water -= int(cells[list_pos][1])
                fire += int(cells[list_pos][1])
            else:
                for_removal.append(list_pos)
        else:
            for_removal.append(list_pos)
    elif cells[list_pos][0] == "Low":
        if 1 <= int(cells[list_pos][1]) <= 50:
            if water >= int(cells[list_pos][1]):
                water -= int(cells[list_pos][1])
                fire += int(cells[list_pos][1])
            else:
                for_removal.append(list_pos)
        else:
            for_removal.append(list_pos)

for pos_pos in range(len(for_removal), 0, -1):
    cells.pop(for_removal[pos_pos - 1])

print("Cells:")
for list_pos in range(0, len(cells)):
    print(f" - {cells[list_pos][1]}")
print(f"Effort: {fire*0.25:.2f}")
print(f"Total Fire: {fire}")


