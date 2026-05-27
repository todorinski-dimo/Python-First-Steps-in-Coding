def grocery_store(**kwargs):
    sorted_products = sorted(kwargs.items(), key = lambda kvp:(-kvp[1], -len(kvp[0]), kvp[0]))
    result_string = ""
    for key, value in sorted_products:
        result_string += f"{key}: {value}\n"
    return result_string



print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    aeges=2,
    pasta=2,
    appls=2,
    eggs=20,
    carrot=1,
))