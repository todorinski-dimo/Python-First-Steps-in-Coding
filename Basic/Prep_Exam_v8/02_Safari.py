budget = float(input())
nights = int(input())
night_price = float(input())
percent_additional_expenses = int(input())

percent_percent_additional_expenses = percent_additional_expenses / 100
additional_expenses = budget * percent_percent_additional_expenses

percent_seven_nights_discount = 0.95
nights_expenses = nights * night_price

if nights > 7:
    nights_expenses *= percent_seven_nights_discount

total_expense = nights_expenses + additional_expenses
delta = abs(budget - total_expense)

if budget >= total_expense:
    print(f"Ivanovi will be left with {delta:.2f} leva after vacation.")
else:
    print(f"{delta:.2f} leva needed.")