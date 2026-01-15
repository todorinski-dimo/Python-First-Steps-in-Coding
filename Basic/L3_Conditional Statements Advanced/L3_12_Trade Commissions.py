city = input()
sales = float(input())
bonus = -1.1

if city == "Sofia":
    if 0 <= sales <= 500:
        bonus = 0.05
    if 500 < sales <= 1000:
        bonus = 0.07
    if 1000 < sales <= 10000:
        bonus = 0.08
    if sales > 10000:
        bonus = 0.12
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        bonus = 0.055
    if 500 < sales <= 1000:
        bonus = 0.08
    if 1000 < sales <= 10000:
        bonus = 0.12
    if sales > 10000:
        bonus = 0.145
elif city == "Varna":
    if 0 <= sales <= 500:
        bonus = 0.045
    if 500 < sales <= 1000:
        bonus = 0.075
    if 1000 < sales <= 10000:
        bonus = 0.1
    if sales > 10000:
        bonus = 0.13

if bonus < 0:
    print("error")
else:
    total = bonus * sales
    print(f"{total:.2f}")
