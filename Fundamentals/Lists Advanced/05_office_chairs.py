rooms = int(input())
available_chairs = []
needed_chairs = []

for room in range(rooms):
    input_data = input().split()
    available_chairs.append(len(input_data[0]))
    needed_chairs.append(int(input_data[1]))
if sum(available_chairs) >= sum(needed_chairs):
    print(f"Game On, {sum(available_chairs) - sum(needed_chairs)} free chairs left")
else:
    for room in range(rooms):
        if needed_chairs[room] - available_chairs[room] > 0:
            print(f"{needed_chairs[room] - available_chairs[room]} more chairs needed in room {room + 1}")