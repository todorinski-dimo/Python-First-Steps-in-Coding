team_a = []
team_b = []
for number in range(1, 12):
    team_a.append("A-" + str(number))
    team_b.append("B-" + str(number))

input_string = input()
input_list = input_string.split()

for player in range(0, len(input_list)):
    if input_list[player] in team_a:
        team_a.remove(input_list[player])
    elif input_list[player] in team_b:
        team_b.remove(input_list[player])
    if len(team_a) < 7 or len(team_b) < 7:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
        print("Game was terminated")
        break
    elif player == len(input_list) - 1:
        print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

