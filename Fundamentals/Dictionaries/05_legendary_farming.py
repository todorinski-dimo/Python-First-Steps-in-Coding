inventory = {"shards":0, "fragments":0, "motes":0}
found = False
while not found:
    init_input = [item.lower() for item in input().split()]
    for idx in range(0, len(init_input), 2):
        key = init_input[idx + 1]
        value = int(init_input[idx])
        if key in inventory:
            inventory[key] += value
        else:
            inventory[key] = value
        if inventory["shards"] >= 250:
            inventory["shards"] -= 250
            print("Shadowmourne obtained!")
            found = True
            break
        if inventory["fragments"] >= 250:
            inventory["fragments"] -= 250
            print("Valanyr obtained!")
            found = True
            break
        if inventory["motes"] >= 250:
            inventory["motes"] -= 250
            print("Dragonwrath obtained!")
            found = True
            break

for k, v in inventory.items():
    print(f"{k}: {v}")
