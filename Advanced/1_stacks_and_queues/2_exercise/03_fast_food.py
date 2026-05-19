from collections import deque

food = int(input())

lst = input().split()
lst = [int(item) for item in lst]

queue = deque(lst)
print(max(queue))

for _ in range(len(queue)):
    order = queue.popleft()
    if food - order >= 0:
        food -= order
    else:
        queue.appendleft(order)
        break

queue = [str(item) for item in queue]

if len(queue) > 0:
    print("Orders left: ", end="")
    print(" ".join(queue))
else:
    print("Orders complete")
