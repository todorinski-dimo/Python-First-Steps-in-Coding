#cars = {
#           "make":{"mileage":"km","fuel":"liters"}
#           "make":{"mileage":"km","fuel":"liters"}
#        }
cars = {}
number_of_cars = int(input())

for _ in range(number_of_cars):
    car = input().split("|")
    car_make = car[0]
    car_mileage = car[1]
    car_fuel = car[2]
    if car_make not in cars.keys():
        cars[car_make] = {"mileage":car_mileage, "fuel":car_fuel}

#print(cars)

cmd = input().split(" : ")
while cmd[0] != "Stop":
    if cmd[0] == "Drive":
        if int(cars[cmd[1]]["fuel"]) >= int(cmd[3]):
            cars[cmd[1]]["fuel"] = int(cars[cmd[1]]["fuel"]) - int(cmd[3])
            cars[cmd[1]]["mileage"] = int(cars[cmd[1]]["mileage"]) + int(cmd[2])
            print(f"{cmd[1]} driven for {cmd[2]} kilometers. {cmd[3]} liters of fuel consumed.")
            if int(cars[cmd[1]]["mileage"]) >= 100000:
                print(f"Time to sell the {cmd[1]}!")
                cars.pop(cmd[1])
        else:
            print("Not enough fuel to make that ride")
    elif cmd[0] == "Refuel":
        fuel = min(75 - int(cars[cmd[1]]["fuel"]), int(cmd[2]))
        print(f"{cmd[1]} refueled with {fuel} liters")
        cars[cmd[1]]["fuel"] = int(cars[cmd[1]]["fuel"]) + fuel
    elif cmd[0] == "Revert":
        if int(cars[cmd[1]]["mileage"]) - int(cmd[2]) < 10000:
            cars[cmd[1]]["mileage"] = 10000
        else:
            cars[cmd[1]]["mileage"] = int(cars[cmd[1]]["mileage"]) - int(cmd[2])
            print(f"{cmd[1]} mileage decreased by {int(cmd[2])} kilometers")
    cmd = input().split(" : ")

for key, data in cars.items():
    print(f"{key} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")
