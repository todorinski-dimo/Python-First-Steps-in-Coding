# contest_pass = {"Part One Interview":"success", "JS Fundamentals":"fundExam", "C# Fundamentals":"fundPass", "Algorithms":"fun"}
# user_score = {"Nikola":{"C# Fundamentals":200, "Part One Interview": 120},
#               "Tanya":{"JS Fundamentals":400, "Algorithms":380, "C# Fundamentals":350, "Part One Interview":220}
#               }

contest_pass = {}
user_score = {}

while True:
    cmd = input().split(":")
    if cmd[0] == "end of contests":
        break
    else:
        contest = cmd[0]
        pas = cmd[1]
        if contest not in contest_pass.keys():
            contest_pass[contest] = ""
        contest_pass[contest] = pas

while True:
    cmd = input().split("=>")
    if cmd[0] == "end of submissions":
        break
    else:
        contest = cmd[0]
        pas = cmd[1]
        user = cmd[2]
        score = int(cmd[3])
        if contest in contest_pass.keys():
            if contest_pass[contest] == pas:
                if user not in user_score.keys():
                    user_score[user] = {}
                if contest not in user_score[user].keys():
                    user_score[user][contest] = 0
                if score > user_score[user][contest]:
                    user_score[user][contest] = score

for user in user_score.keys():
    if "total_score" not in user_score[user].keys():
        user_score[user]["total_score"] = 0

for user in user_score.keys():
    for contest, score in user_score[user].items():
        if contest != "total_score":
            user_score[user]["total_score"] += score

best_score = 0
best_candidate = ""
for user in user_score.keys():
    if user_score[user]["total_score"] > best_score:
        best_score = user_score[user]["total_score"]
        best_candidate = user

print(f"Best candidate is {best_candidate} with total {best_score} points.")

user_score = {user:score for user, score in sorted(user_score.items(), key=lambda item: item[0])}
for user in user_score.keys():
    user_score[user] = {contest:score for contest, score in sorted(user_score[user].items(), key=lambda item: -item[1])}

print("Ranking:")
for user in user_score.keys():
    print(user)
    for contest, score in user_score[user].items():
        if contest != "total_score":
            print(f"#  {contest} -> {score}")
