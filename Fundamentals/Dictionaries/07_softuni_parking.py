parking_log_register = {}
cycles = int(input())

for _ in range(cycles):
    cmd = input().split()
    if cmd[0] == "register":
        username = cmd[1]
        license_plate = cmd[2]
        if username in parking_log_register:
            print(f"ERROR: already registered with plate number {parking_log_register[username]}")
        else:
            parking_log_register[username] = license_plate
            print(f"{username} registered {parking_log_register[username]} successfully")
    if cmd[0] == "unregister":
        username = cmd[1]
        if username in parking_log_register:
            del parking_log_register[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for username, license_plate in parking_log_register.items():
    print(f"{username} => {license_plate}")
