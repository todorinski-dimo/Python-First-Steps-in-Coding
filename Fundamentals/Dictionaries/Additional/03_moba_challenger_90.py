# player_skills = {
#                 "Player1":{"position1":"skill", "position2":"skill", "position3":"skill"},
#                 "Player2":{"position1":"skill", "position2":"skill", "position4":"skill"}
#                  }
# player_skills_total = {"Player1":"total_skill", "Player2":"total_skill"}

player_skills = {}
player_skills_total = {}

while True:
    cmd = input()
    if cmd == "Season end":
        break
    elif "->" in cmd:
        cmd = cmd.split(" -> ")
        player = cmd[0]
        position = cmd[1]
        skill = int(cmd[2])
        if player not in player_skills.keys():
            player_skills[player] = {}
            player_skills_total[player] = 0
        if position not in player_skills[player].keys():
            player_skills[player][position] = 0
        if skill > player_skills[player][position]:
            player_skills_total[player] += skill - player_skills[player][position]
            player_skills[player][position] = skill
        # print(player_skills)
        # print(player_skills_total)

    elif "vs" in cmd:
        cmd = cmd.split(" vs ")
        player1 = cmd[0]
        player2 = cmd[1]
        if (player1 in player_skills.keys() and player2 in player_skills.keys() and
                player_skills_total[player1] != player_skills_total[player2]):
            for position2 in player_skills[player2].keys():
                for position1 in player_skills[player1].keys():
                    if position1 == position2:
                        if player_skills_total[player1] > player_skills_total[player2]:
                            del player_skills[player2]
                            del player_skills_total[player2]
                        else:
                            del player_skills[player1]
                            del player_skills_total[player1]
                        # print(player_skills)
                        # print(player_skills_total)

player_skills_total = {player:points for player, points in
                       sorted(player_skills_total.items(), key=lambda item: -item[1])}
# print(player_skills_total)
for player in player_skills.keys():
    player_skills[player] = {position:points for position, points in
                             sorted(player_skills[player].items(), key=lambda item: item[0])}
    player_skills[player] = {position:points for position, points in
                             sorted(player_skills[player].items(), key=lambda item: -item[1])}

# print(player_skills)
# print(player_skills_total)
for player, points in player_skills_total.items():
    print(f"{player}: {points} skill")
    for position, points_ in player_skills[player].items():
        print(f"- {position} <::> {points_}")

