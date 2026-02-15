countries = input().split(", ")
capitals = input().split(", ")

# output = dict(zip(countries, capitals))
output = {co:ca for (co,ca) in zip(countries,capitals)}

for country, capital in output.items():
    print(f"{country} -> {capital}")