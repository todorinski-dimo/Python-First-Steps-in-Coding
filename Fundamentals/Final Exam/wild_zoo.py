# animals = {
#           "animal_name":{"needed_food_quantity":"quantity", "area":"area_name"}
#           }

animals = {}
animal = []
areas = {}
cmd = input().split(": ")
if cmd[0] != "EndDay":
    animal = cmd[1].split("-")
# print(cmd)
# print(animal)

while cmd[0] != "EndDay":
    if cmd[0] == "Add":
        if animal[0] in animals:
            animals[animal[0]]["needed_food_quantity"] = int(animals[animal[0]]["needed_food_quantity"]) + int(animal[1])
        else:
            animals[animal[0]] = {}
            animals[animal[0]]["needed_food_quantity"] = animal[1]
            animals[animal[0]]["area"] = animal[2]
            if animal[2] in areas:
                areas[animal[2]] = int(areas[animal[2]]) + 1
            else:
                areas[animal[2]] = "1"

    elif cmd[0] == "Feed":
        if animal[0] in animals:
            animals[animal[0]]["needed_food_quantity"] = int(animals[animal[0]]["needed_food_quantity"]) - int(animal[1])
            if int(animals[animal[0]]["needed_food_quantity"]) <= 0:
                area = animals[animal[0]]["area"]
                areas[area] = int(areas[area]) - 1
                animals.pop(animal[0])
                print(f"{animal[0]} was successfully fed")

    cmd = input().split(": ")
    if cmd[0] != "EndDay":
        animal = cmd[1].split("-")
    # print(cmd)
    # print(animal)

# print(animals)
print("Animals:")
for name, data in animals.items():
    print(f" {name} -> {data['needed_food_quantity']}g")
print("Areas with hungry animals:")
for name, data in areas.items():
    if data != 0:
        print(f" {name}: {data}")
