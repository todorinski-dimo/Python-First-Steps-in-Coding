def concatenate(*args, **kwargs):
    init_string = ""

    for item in args:
        init_string += item
    for key, value in kwargs.items():
        if key in init_string:
            init_string = init_string.replace(key, kwargs[key])

    return init_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))