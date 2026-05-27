def kwargs_length(**kwargs):
    # for key, value in kwargs.items():
    #     print(key, value)
    return len(kwargs)

dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))