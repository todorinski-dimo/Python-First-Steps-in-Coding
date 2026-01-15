days_to_birthday = 5

daily_allowance = float(input())
daily_profit = float(input())
total_expenses = float(input())
present_cost = float(input())

profit = days_to_birthday * (daily_allowance + daily_profit)
total_profit = profit - total_expenses
delta = abs(present_cost - total_profit)

if total_profit >= present_cost:
    print(f"Profit: {total_profit:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {delta:.2f} BGN.")