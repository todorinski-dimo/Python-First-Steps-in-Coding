fuel_type = input()
fuel_qty = float(input())

fuel_type2 = ""

if fuel_type == "Gasoline":
    fuel_type2 = "gasoline"
elif fuel_type == "Gas":
    fuel_type2 = "gas"
elif fuel_type == "Diesel":
    fuel_type2 = "diesel"

if fuel_qty >= 25 and (fuel_type == "Gasoline" or fuel_type == "Diesel" or fuel_type == "Gas"):
    print(f"You have enough {fuel_type2}.")
elif fuel_qty < 25 and (fuel_type == "Gasoline" or fuel_type == "Diesel" or fuel_type == "Gas"):
    print(f"Fill your tank with {fuel_type2}!")
else:
    print("Invalid fuel!")
