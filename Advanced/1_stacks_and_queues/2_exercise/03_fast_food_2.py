from collections import deque

food = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders and orders[0] <= food:
    food -= orders.popleft()

if orders:
    print("Orders left:", *orders)
else:
    print("Orders Complete")