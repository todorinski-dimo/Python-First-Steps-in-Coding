budget = float(input())
statists = int(input())
clothes_price = float(input())

decor = budget * 0.1
clothes_cost = statists * clothes_price

if statists > 150:
    clothes_cost *= 0.9

total_cost = decor + clothes_cost

savings = budget - total_cost

if savings >= 0:
    print("Action!")
    print(f"Wingard starts filming with {savings:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(savings):.2f} leva more.")