from collections import deque

queue = deque()
init_water = int(input())

while True:
    input_string = input()
    if input_string == "Start":
        break
    else:
        queue.append(input_string)

while True:
    input_string = input()
    if input_string.isdigit():
        person = queue.popleft()
        water_needed = int(input_string)
        if water_needed <= init_water:
            init_water -= water_needed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    elif input_string.split()[0] == "refill":
        init_water += int(input_string.split()[1])
    elif input_string == "End":
        print(f"{init_water} liters left")
        break
