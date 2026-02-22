# dragons = [
#     {"type":"Red", "name":"Bazgargal", "damage":100, "health":2500, "armor":25},
#     {"type":"Black", "name":"Dargonax", "damage":200, "health":3500, "armor":18}
# ]
# stats = {type:{"avg_damage":avg_damage, "avg_health":avg_health, "avg_armor":avg_armor},
#          type1:{"avg_damage":avg_damage, "avg_health":avg_health, "avg_armor":avg_armor}
#          }

items = []
stats = {}
default_damage = 45
default_health = 250
default_armor = 10


numb_item = int(input())

for _ in range(numb_item):
    item_exists = False
    input_item = input().split(" ")
    type_ = input_item[0]
    name_ = input_item[1]

    if input_item[2] == "null":
        damage_ = default_damage
    else:
        damage_ = int(input_item[2])

    if input_item[3] == "null":
        health_ = default_health
    else:
        health_ = int(input_item[3])

    if input_item[4] == "null":
        armor_ = default_armor
    else:
        armor_ = int(input_item[4])

    for item in items:
        if item["type"]+item["name"] == type_+name_:
            item_exists = True
    if item_exists:
        for item in items:
            if item["type"] + item["name"] == type_ + name_:
                item["damage"] = damage_
                item["health"] = health_
                item["armor"] = armor_
    else:
        items.append({"type":type_, "name":name_, "damage":damage_, "health":health_, "armor":armor_})

# print(items)

for item in items:
    if item["type"] not in stats.keys():
        stats[item["type"]] = {}
        stats[item["type"]]["count"] = 0
        stats[item["type"]]["sum_dmg"] = 0
        stats[item["type"]]["sum_hlt"] = 0
        stats[item["type"]]["sum_arm"] = 0
        stats[item["type"]]["avg_dmg"] = 0
        stats[item["type"]]["avg_hlt"] = 0
        stats[item["type"]]["avg_arm"] = 0
    if item["type"] in stats.keys():
        stats[item["type"]]["count"] += 1
        stats[item["type"]]["sum_dmg"] += item["damage"]
        stats[item["type"]]["sum_hlt"] += item["health"]
        stats[item["type"]]["sum_arm"] += item["armor"]

for key in stats.keys():
    stats[key]["avg_dmg"] = stats[key]["sum_dmg"]/stats[key]["count"]
    stats[key]["avg_hlt"] = stats[key]["sum_hlt"]/stats[key]["count"]
    stats[key]["avg_arm"] = stats[key]["sum_arm"]/stats[key]["count"]

# print(items)
#
# print(stats)

items = sorted(items, key=lambda sort_by: sort_by["name"])

for key in stats.keys():
    print(f"{key}::({stats[key]['avg_dmg']:.2f}/{stats[key]['avg_hlt']:.2f}/{stats[key]['avg_arm']:.2f})")
    for item in items:
        if key == item["type"]:
            print(f"-{item['name']} -> damage: {item['damage']}, health: {item['health']}, armor: {item['armor']}")
