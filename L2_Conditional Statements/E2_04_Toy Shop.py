puzzle_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

expense_budget = float(input())
puzzle_qty = int(input())
doll_qty = int(input())
bear_qty = int(input())
minion_qty = int(input())
truck_qty = int(input())

total_qty = puzzle_qty + doll_qty + bear_qty + minion_qty + truck_qty
total_turnover = puzzle_price * puzzle_qty + doll_price * doll_qty + bear_price * bear_qty + minion_qty * minion_price \
                 + truck_price*truck_qty

if total_qty >= 50:
    total_turnover *= 0.75

total_turnover *= 0.9

leftover = abs(total_turnover - expense_budget)

if total_turnover - expense_budget >= 0:
    print(f"Yes! {leftover:.2f} lv left.")
else:
    print(f"Not enough money! {leftover:.2f} lv needed.")