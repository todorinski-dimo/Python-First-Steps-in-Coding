target = int(input())

income = 0

while True:
    service_type = input()
    if service_type == "closed":
        if income >= target:
            print("You have reached your target for the day!")
            print(f"Earned money: {income}lv.")
        else:
            print(f"Target not reached! You need {target-income}lv. more.")
            print(f"Earned money: {income}lv.")
        break
    service_subtype = input()
    if service_type == "haircut":
        if service_subtype == "mens":
            income += 15
        elif service_subtype == "ladies":
            income += 20
        elif service_subtype == "kids":
            income += 10
    elif service_type == "color":
        if service_subtype == "touch up":
            income += 20
        elif service_subtype == "full color":
            income += 30
    if income >= target:
        print("You have reached your target for the day!")
        print(f"Earned money: {income}lv.")
        break
