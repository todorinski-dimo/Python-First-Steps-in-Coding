from collections import deque

queue = deque(input().split())
steps = int(input())

while len(queue) != 1:
    queue.rotate(-steps + 1)
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue.pop()}")