age = float(input())
gender = input()

if age >= 16:
    if gender == "m":
        print("Mr.")
    if gender == "f":
        print("Ms.")
else:
    if gender == "m":
        print("Master")
    if gender == "f":
        print("Miss")