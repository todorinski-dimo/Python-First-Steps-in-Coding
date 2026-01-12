budget = float(input())
n = int(input())
m = int(input())
p = int(input())

n_price = 250
m_price = n * n_price * 0.35
p_price = n * n_price * 0.1

cost = n * n_price + m * m_price + p * p_price
if n > m:
    cost *= 0.85
savings = abs(budget - cost)

if budget >= cost:
    print(f"You have {savings:.2f} leva left!")
else:
    print(f"Not enough money! You need {savings:.2f} leva more!")