companies = {}

while True:
    cmd = input().split(" -> ")
    if cmd[0] == "End":
        for company, user in companies.items():
            print(f"{company}")
            for users in companies[company]:
                print(f"-- {users}")
        break
    else:
        company = cmd[0]
        user = cmd[1]
        if company in companies:
            if user not in companies[company]:
                companies[company].append(user)
        else:
            companies[company] = [user]
