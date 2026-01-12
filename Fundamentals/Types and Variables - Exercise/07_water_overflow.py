cycles = int(input())
capacity = 255
poured = 0
pour = 0

for _ in range(cycles):
    pour = int(input())
    if poured + pour <= capacity:
        poured += pour
    else:
        print("Insufficient capacity!")

print(poured)