def plant_garden(area:float, *args:tuple, **kwargs:dict) -> str:
    requested_plants = kwargs
    requested_plants_count = 0
    allowed_plants = {}
    for item in args:
        allowed_plants[item[0]] = item[1]
    for plant in requested_plants:
        if plant in allowed_plants.keys():
            requested_plants_count += requested_plants[plant]
    planted = {}
    for plant in requested_plants:
        if plant in allowed_plants.keys():
            plants_for_panting = allowed_plants[plant]
            for _ in range(plants_for_panting):
                if allowed_plants[plant] <= area and requested_plants_count > 0:
                    area -= allowed_plants[plant]
                    if plant not in planted.keys():
                        planted[plant] = 0
                    planted[plant] += 1
                    requested_plants_count -= 1
    result = ""
    if requested_plants_count == 0:
        result += f"All plants were planted! Available garden space: {area:.1f} sq meters.\n"
    else:
        result += f"Not enough space to plant all requested plants!\n"

    result += "Planted plants:"
    for plant in sorted(planted):
        result += f"\n{plant}: {planted[plant]}"
    return result



print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
