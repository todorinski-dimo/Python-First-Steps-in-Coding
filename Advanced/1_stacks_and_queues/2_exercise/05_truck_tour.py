from collections import deque
petrol_stations = int(input())
petrol_stations_deque = deque()

for _ in range(petrol_stations):
    fuel, distance = [int(x) for x in input().split()]
    petrol_stations_deque.append([fuel, distance])

start_position = 0
counter = 0

while counter < petrol_stations:
    current_fuel = 0
    for i in range(petrol_stations):
        current_fuel += petrol_stations_deque[i][0]
        distance = petrol_stations_deque[i][1]
        if current_fuel < distance:
            counter = 0
            start_position += 1
            petrol_stations_deque.rotate(-1)
            break
        current_fuel -= distance
        counter +=1

print(start_position)
