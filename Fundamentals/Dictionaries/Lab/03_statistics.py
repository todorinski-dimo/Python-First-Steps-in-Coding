items = {}

while True:
    cmd = input().split(": ")
    if cmd[0] == "statistics":
        print("Products in stock:")
        for key, value in items.items():
            print(f"- {key}: {value}")
        print(f"Total Products: {len(items.keys())}")
        print(f"Total Quantity: {sum(items.values())}")
        break
    else:
        key = cmd[0]
        value = int(cmd[1])
        if key in items:
            items[key] += value
        else:
            items[key] = value
