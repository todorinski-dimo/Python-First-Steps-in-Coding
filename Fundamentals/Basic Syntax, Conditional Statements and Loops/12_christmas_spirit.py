price_os = 2
spirit_os = 5
price_ts = 5
spirit_ts = 3
price_tg = 3
spirit_tg = 10
price_tl = 15
spirit_tl = 17

pcs_day = int(input())
days_to_christmas = int(input())

budget = 0
spirit = 0
day = 1

while day != days_to_christmas + 1:
    if day % 11 == 0:
        pcs_day += 2
    if day % 2 == 0:
        budget += pcs_day * price_os
        spirit += spirit_os
    if day % 3 == 0:
        budget += pcs_day * (price_ts + price_tg)
        spirit += spirit_ts + spirit_tg
    if day % 5 == 0:
        budget += pcs_day * price_tl
        spirit += spirit_tl
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += price_ts + price_tl + price_tg
    day += 1
if days_to_christmas % 10 == 0:
    spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")

