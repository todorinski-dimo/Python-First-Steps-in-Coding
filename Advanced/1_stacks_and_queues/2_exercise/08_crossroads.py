from collections import deque

green_light = int(input())
free_window = int(input())

car_queue = deque()
cars_passed = 0
current_green = green_light
crash = False

while True:
    command = input()
    if command == "END":
        print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")
        break
    if command != "green":
        car_queue.append(command)
        continue

    current_green = green_light

    while car_queue and current_green > 0:
        car = car_queue.popleft()
        car_length = len(car)
        if car_length <= current_green:
            cars_passed +=1
            current_green -= car_length
        else:
            car_rem = car_length - current_green
            if car_rem <= free_window:
                cars_passed += 1
                break
            else:
                hit_index = current_green + free_window
                print(f"A crash happened!\n{car} was hit at {car[hit_index]}.")
                crash = True
                break

    if crash:
        break




