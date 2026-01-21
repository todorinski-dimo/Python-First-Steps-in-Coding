type_price_list = input().split("|")
type_price_modlist = []
budget = float(input())

budget_left = budget
clothes_limit_price = 50
shoes_limit_price = 35
accessories_limit_price = 20.50
price_increase = 1.4


new_prices_list = []

for couple in range(0, len(type_price_list)):
    type_price_modlist.append(type_price_list[couple].split("->"))

for item in range(0, len(type_price_modlist)):
    if type_price_modlist[item][0] == "Clothes":
        if float(type_price_modlist[item][1]) <= clothes_limit_price:
            if budget_left >= float(type_price_modlist[item][1]):
                budget_left -= float(type_price_modlist[item][1])
                new_prices_list.append(float(type_price_modlist[item][1])*price_increase)
    if type_price_modlist[item][0] == "Shoes":
        if float(type_price_modlist[item][1]) <= shoes_limit_price:
            if budget_left >= float(type_price_modlist[item][1]):
                budget_left -= float(type_price_modlist[item][1])
                new_prices_list.append(float(type_price_modlist[item][1])*price_increase)
    if type_price_modlist[item][0] == "Accessories":
        if float(type_price_modlist[item][1]) <= accessories_limit_price:
            if budget_left >= float(type_price_modlist[item][1]):
                budget_left -= float(type_price_modlist[item][1])
                new_prices_list.append(float(type_price_modlist[item][1])*price_increase)

for price in range(0, len(new_prices_list)):
    print(f"{new_prices_list[price]:.2f} ", end="")

final_budget = budget_left + (budget - budget_left)*price_increase
profit = final_budget - budget
print("")
print(f"Profit: {profit:.2f}")
if final_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


