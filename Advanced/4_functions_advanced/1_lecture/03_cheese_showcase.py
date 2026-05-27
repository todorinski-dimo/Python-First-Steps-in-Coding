def sorting_cheeses(**kwargs):
    sorted_list = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""

    for cheese, quantities in sorted_list:
        result += f"{cheese}\n"
        for quantity in sorted(quantities, reverse=True):
            result += f"{quantity}\n"

    return result

print(
        sorting_cheeses(
            Parmesan=[102, 120, 135],
            Camembert=[100, 100, 105, 500, 430],
            Mozzarella=[50, 125],
        )
    )

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)