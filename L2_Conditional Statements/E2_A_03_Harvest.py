from math import floor
from math import ceil

total_area = int(input())
grapes_production_rate = float(input())
wine_for_sell = int(input())
workers_count = int(input())

wine_production_rate = 2.5

grapes_for_wine = 0.4 * (total_area * grapes_production_rate)
produced_wine = grapes_for_wine / wine_production_rate

delta = abs(wine_for_sell - produced_wine)
delta_per_worker = delta / workers_count

if produced_wine < wine_for_sell:
    print(f'It will be a tough winter! More {floor(delta)} liters wine needed.')
else:
    print(f"Good harvest this year! Total wine: {floor(produced_wine)} liters.")
    print(f"{ceil(delta)} liters left -> {ceil(delta_per_worker)} liters per person.")