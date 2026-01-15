from math import floor as rounddown
from math import ceil as roundup

m_price = 3.25
z_price = 4
r_price = 3.5
c_price = 8

m_qty = int(input())
z_qty = int(input())
r_qty = int(input())
c_qty = int(input())
gift_cost = float(input())

flower_cost = m_qty * m_price + z_qty * z_price + r_qty * r_price + c_qty * c_price
flower_cost *= 0.95

saving = abs(flower_cost - gift_cost)

if flower_cost - gift_cost >=0:
    print(f"She is left with {rounddown(saving)} leva.")
else:
    print(f"She will have to borrow {roundup(saving)} leva.")
