# user_score = {
#                  "contest_name1":{"username1":"points", "username2":"points" },
#                  "contest_name2":{"username1":"points", "username3":"points" }
#               }

user_score = {}

while True:
    cmd = input().split(" -> ")
    if cmd[0] == "no more time":
        break
    else:
        user = cmd[0]
        contest = cmd[1]
        score = int(cmd[2])
        if contest not in user_score.keys():
            user_score[contest] = {}
        if user not in user_score[contest].keys():
            user_score[contest][user] = score
        elif score > user_score[contest][user]:
            user_score[contest][user] = score

# print(user_score)

for contest in user_score.keys():
    user_score[contest] = {user:points for user, points in sorted(user_score[contest].items(), key=lambda item: item[0])}
for contest in user_score.keys():
    user_score[contest] = {user:points for user, points in sorted(user_score[contest].items(), key=lambda item: -item[1])}

# print(user_score)

for contest, data in user_score.items():
    print(f"{contest}: {len(data)} participants")
    counter = 0
    for user, points in user_score[contest].items():
        counter += 1
        print(f"{counter}. {user} <::> {points}")

user_score_totals = {}
for contest in user_score.keys():
    for user, points in user_score[contest].items():
        if user not in user_score_totals.keys():
            user_score_totals[user] = 0
        user_score_totals[user] += points

# print(user_score_totals)

user_score_totals = {user:points for user, points in sorted(user_score_totals.items(), key=lambda item: item[0])}
user_score_totals = {user:points for user, points in sorted(user_score_totals.items(), key=lambda item: -item[1])}

# print(user_score_totals)
counter = 0
print("Individual standings:")
for user, points in user_score_totals.items():
    counter += 1
    print(f"{counter}. {user} -> {points}")