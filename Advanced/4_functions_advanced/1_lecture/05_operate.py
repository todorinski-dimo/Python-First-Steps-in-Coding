from functools import reduce

def num_sum(*args):
    return reduce(lambda x, y: x + y, args)
def num_diff(*args):
    return reduce(lambda x, y: x - y, args)
def num_multy(*args):
    return reduce(lambda x, y: x * y, args)
def num_div(*args):
    return reduce(lambda x, y: x / y, args)

mapper = {
    "+": num_sum,
    "-": num_diff,
    "*": num_multy,
    "/": num_div,
}

def operate(operator, *args):
    func = mapper[operator]
    return func(*args)

print(operate("+", 1, 2, 3))
print(operate("/", 3, 4))