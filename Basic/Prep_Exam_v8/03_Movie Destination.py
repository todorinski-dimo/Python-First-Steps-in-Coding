budget = float(input())
destination = input()
season = input()
days = int(input())

price_per_day = 0

dubai_discount = 0.7
sofia_discount = 1.25

if season == "Winter":
    if destination == "London":
        price_per_day = 24000
    elif destination == "Sofia":
        price_per_day = 17000 * sofia_discount
    elif destination == "Dubai":
        price_per_day = 45000 * dubai_discount
elif season == "Summer":
    if destination == "London":
        price_per_day = 20250
    elif destination == "Sofia":
        price_per_day = 12500 * sofia_discount
    elif destination == "Dubai":
        price_per_day = 40000 * dubai_discount

total_cost = price_per_day * days
delta = abs(budget - total_cost)

if budget >= total_cost:
    print(f"The budget for the movie is enough! We have {delta:.2f} leva left!")
else:
    print(f"The director needs {delta:.2f} leva more!")