electrons = int(input())
counter = 0
shells = []

while electrons > 0:
    counter += 1
    if electrons >= 2 * (counter ** 2):
        shells.append(2 * (counter ** 2))
    elif 0 <= electrons < 2 * (counter ** 2):
        shells.append(electrons)
    electrons -= 2 * (counter ** 2)

print(shells)