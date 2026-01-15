package_weight = float(input())
type_service = input()
km = float(input())

rate1 = 0.03
rate2 = 0.05
rate3 = 0.1
rate4 = 0.15
rate5 = 0.2

cost = 0
sub_cost = 0

if package_weight < 1:
    if type_service == "standard":
        cost = rate1 * km
    elif type_service == "express":
        cost = (rate1 * km) + (rate1 * 0.8 * km * package_weight)
elif package_weight < 10:
    if type_service == "standard":
        cost = rate2 * km
    elif type_service == "express":
        cost = (rate2 * km) + (rate2 * 0.4 * km * package_weight)
elif package_weight < 40:
    if type_service == "standard":
        cost = rate3 * km
    elif type_service == "express":
        cost = (rate3 * km) + (rate3 * 0.05 * km * package_weight)
elif package_weight < 90:
    if type_service == "standard":
        cost = rate4 * km
    elif type_service == "express":
        cost = (rate4 * km) + (rate4 * 0.02 * km * package_weight)
elif package_weight < 150:
    if type_service == "standard":
        cost = rate5 * km
    elif type_service == "express":
        cost = (rate5 * km) + (rate5 * 0.01 * km * package_weight)

print(f"The delivery of your shipment with weight of {package_weight:.3f} kg. would cost {cost:.2f} lv.")