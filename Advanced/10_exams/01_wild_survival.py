from collections import deque

EATER_POWER = 7

bees = deque(map(int, input().split()))
eaters = [int(group) for group in input().split()]


while bees and eaters:
    while bees[0] > 0 and eaters[-1] > 0:
        bees[0] -= 7
        if bees[0] >= 0:
            eaters[-1] -= 1
    if bees[0] > 0 and eaters[-1] < 1:
        bees.rotate(-1)
    if bees[0] < 1:
        bees.popleft()
    if eaters[-1] < 1:
        eaters.pop()

print("The final battle is over!")
if not bees and not eaters:
    print("But no one made it out alive!")
elif bees:
    print(f"Bee groups left: {', '.join(map(str, bees))}")
else:
    print(f"Bee-eater groups left: {', '.join(map(str, eaters))}")
