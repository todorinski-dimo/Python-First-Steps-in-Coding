def age_assignment(*args, **kwargs):
    result = {}
    sorted_result = []
    for key, value in kwargs.items():
        for item in args:
            if item[0] == key:
                result[item]=value
    result = sorted(result.items(), key=lambda kvp: kvp[0])
    for key, value in result:
        sorted_result.append(f"{key} is {value} years old.")
    return "\n".join(sorted_result)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))