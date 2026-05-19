from collections import deque

queue = deque()

while True:
    input_string = input()
    if input_string == "End":
        break
    elif input_string == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(input_string)

print(f"{len(queue)} people remaining.")