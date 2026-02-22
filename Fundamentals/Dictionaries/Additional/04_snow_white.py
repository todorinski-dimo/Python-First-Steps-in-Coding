# dwarfs = [
#     {"name":"Grumpy", "color":"Red", "size":10000},
#     {"name":"Grumpy", "color":"Blue", "size":10000},
#     {"name":"Happy", "color":"Blue", "size":10000}
# ]

dwarfs = []
has_same_name_color = False
has_same_name_color_size = False

while True:
    cmd = input().split(" <:> ")
    if cmd[0] == "Once upon a time":
        break
    else:
        has_same_name_color = False
        has_same_name_color_size = False
        name_ = cmd[0]
        color_ = cmd[1]
        size_ = int(cmd[2])
        for item in dwarfs:
            # print(item["name"]+item["color"])
            # print(item["size"])
            # print(name_+str(size_))
            if name_+color_ == item["name"]+item["color"]:
                has_same_name_color = True
            if name_+color_ == item["name"]+item["color"] and size_ > item["size"]:
                has_same_name_color_size = True
        # print(has_same_name_color, has_same_name_color_size)
        if has_same_name_color and has_same_name_color_size:
            for item in dwarfs:
                if name_+color_ == item["name"]+item["color"] and size_ > int(item["size"]):
                    item["size"] = size_
        if not has_same_name_color:
            dwarfs.append({"name": name_, "color": color_, "size": size_})
        # print(dwarfs)

sorted_dwarfs = sorted(dwarfs, key=lambda sort_by: (-sort_by["size"], sort_by['color']))

for item in sorted_dwarfs:
    print(f"({item['color']}) {item['name']} <-> {item['size']}")
