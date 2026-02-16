users_points = {}
lang_submissions = {}

while True:
    cmd = input().split("-")
    if cmd[0] == "exam finished":
        print("Results:")
        for user, score in users_points.items():
            print(f"{user} | {score}")
        print("Submissions:")
        for lang, sub in lang_submissions.items():
            print(f"{lang} - {sub}")
        break
    elif cmd[1] == "banned":
        user = cmd[0]
        if user in users_points.keys():
            del users_points[user]
    else:
        user = cmd[0]
        lang = cmd[1]
        score = int(cmd[2])
        if lang not in lang_submissions.keys():
            lang_submissions[lang] = 0
        lang_submissions[lang] += 1
        if user not in users_points.keys():
            users_points[user] = 0
        if score > users_points[user]:
            users_points[user] = score
