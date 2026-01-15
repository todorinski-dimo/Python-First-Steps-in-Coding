product = input()
weekday = input()
quantity = float(input())
price = 0

if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" or weekday == "Friday":
    if product == "banana":
        price = 2.5
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "apple":
        price = 1.2
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "orange":
        price = 0.85
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "grapefruit":
        price = 1.45
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "kiwi":
        price = 2.7
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "pineapple":
        price = 5.5
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "grapes":
        price = 3.85
        value = price * quantity
        print(f"{value:.02f}")
    else:
        print("error")
elif weekday == "Saturday" or weekday == "Sunday":
    if product == "banana":
        price = 2.7
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "apple":
        price = 1.25
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "orange":
        price = 0.9
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "grapefruit":
        price = 1.6
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "kiwi":
        price = 3
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "pineapple":
        price = 5.6
        value = price * quantity
        print(f"{value:.02f}")
    elif product == "grapes":
        price = 4.2
        value = price * quantity
        print(f"{value:.02f}")
    else:
        print("error")
else:
    print("error")

