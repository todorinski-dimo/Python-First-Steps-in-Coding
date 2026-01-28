numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# map() needs to have a function as attribute that always return values for each initial list, even if "if" is used
mapped_numbers = list(map(lambda item: item ** 2, numbers))
print(f"mapped_number: {mapped_numbers}")

# filter() function-attribute needs to have true or 1 to return a value, others will be filtered
filtered_numbers = list(filter(lambda item: item % 2 == 0, numbers))
print(f"filtered_numbers: {filtered_numbers}")
filtered_numbers_non_bool = list(filter(lambda item: item / 3, numbers))
print(f"filtered_numbers: {filtered_numbers_non_bool}")

# map() needs to have a function as attribute that always return values for each initial list, even if "if" is used
map_as_filter = list(map(lambda item: item if item % 2 == 0 else None, numbers))
print(f"map_as_filer: {map_as_filter}")
