from collections import deque

price_bullet = int(input())
magazine_size = int(input())
bullets = [int(item) for item in input().split()]
locks = deque(int(item) for item in input().split())
prise = int(input())

current_magazine = magazine_size
while locks and bullets:
    current_bullet = bullets.pop()
    current_magazine -= 1
    prise -= price_bullet
    if current_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    if current_magazine == 0 and bullets:
        print("Reloading!")
        current_magazine += magazine_size

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${prise}")