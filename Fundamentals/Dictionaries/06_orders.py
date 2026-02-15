inventory = {}

while True:
    cmd = input().split()
    if cmd[0] == "buy":
        for k,v in inventory.items():
            print(f"{k} -> {inventory[k][0] * inventory[k][1]:.2f}")
        break
    else:
        product = cmd[0]
        price_qty = [float(cmd[1]), float(cmd[2])]
        if product in inventory:
            inventory[product][0] = price_qty[0]
            inventory[product][1] += price_qty[1]
        else:
            inventory[product] = price_qty
