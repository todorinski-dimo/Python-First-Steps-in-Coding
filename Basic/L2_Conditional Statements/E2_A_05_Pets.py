from math import floor as rounddown
from math import ceil as roundup
days_qty = int(input())
total_food_qty = int(input())
dog_food_rate = float(input())
cat_food_rate = float(input())
turtle_food_rate = float(input())

turtle_food_rate /= 1000

total_consumption = (dog_food_rate + cat_food_rate + turtle_food_rate) * days_qty

savings = abs(total_food_qty - total_consumption)

if total_food_qty - total_consumption >= 0:
    print(f"{rounddown(savings)} kilos of food left.")
else:
    print(f"{roundup(savings)} more kilos of food are needed.")