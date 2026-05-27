def even_odd(*args):
    numbers = [int(item) for item in args[:-1]]
    def even():
        return [item for item in numbers if item % 2 == 0]
    def odd():
        return [item for item in numbers if item % 2 != 0]

    if args[-1] == "even":
        return even()
    elif args[-1] == "odd":
        return odd()
    return None

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))