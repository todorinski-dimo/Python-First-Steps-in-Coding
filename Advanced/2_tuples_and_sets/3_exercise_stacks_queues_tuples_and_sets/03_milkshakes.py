from collections import deque

choco_decrease = 5
successes = 5

chocos = [int(item) for item in input().split(", ")]
milks = deque(int(item) for item in input().split(", "))

milkshakes = 0

while chocos and milks and milkshakes < successes:
    choco = chocos[-1]
    milk = milks[0]

    if choco <= 0 or milk <= 0:
        if choco <= 0:
            chocos.pop()
        if milk <= 0:
            milks.popleft()
        continue

    if choco == milk:
        milkshakes += 1
        chocos.pop()
        milks.popleft()
    else:
        milks.rotate(-1)
        chocos[-1] -= choco_decrease

if milkshakes == successes:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
print(f"Chocolate: {', '.join(map(str, chocos)) if chocos else 'empty'}")
print(f"Milk: {', '.join(map(str, milks)) if milks else 'empty'}")