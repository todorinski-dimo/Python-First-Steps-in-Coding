petrol_price = 2.22
diesel_price = 2.33
lpg_price = 0.93

fuel_type = input()
fuel_qty = float(input())
smart_card = input()

discount_total = 1
cost = 0

if fuel_qty > 25:
    discount_total = 0.9
elif 20 <= fuel_qty <= 25:
    discount_total = 0.92
else:
    discount_total = 1

if smart_card == "Yes":
    if fuel_type == "Gasoline":
        cost = (petrol_price - 0.18) * fuel_qty
    elif fuel_type == "Diesel":
        cost = (diesel_price - 0.12) * fuel_qty
    elif fuel_type == "Gas":
        cost = (lpg_price - 0.08) * fuel_qty
elif smart_card == "No":
    if fuel_type == "Gasoline":
        cost = (petrol_price) * fuel_qty
    elif fuel_type == "Diesel":
        cost = (diesel_price) * fuel_qty
    elif fuel_type == "Gas":
        cost = (lpg_price) * fuel_qty

total_cost = cost * discount_total

print(f"{total_cost:.2f} lv.")