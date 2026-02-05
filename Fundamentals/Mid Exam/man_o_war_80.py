# https://alpha.judge.softuni.org/contests/06-programming-fundamentals-mid-exam-retake/1773/practice#3
# score 80

pirate_status = [int(item) for item in input().split(">")]
man_o_war_status = [int(item) for item in input().split(">")]
max_health_section = int(input())
is_for_repair = 0.2
pirate_for_repair_sections = 0
pirate_ship_sum = 0
man_o_war_ship_sum = 0
ship = True

while ship:
    cmd = input()
    if cmd == "Retire":
        pirate_ship_sum = sum(pirate_status)
        man_o_war_ship_sum = sum(man_o_war_status)
        print(f"Pirate ship status: {pirate_ship_sum}")
        print(f"Warship status: {man_o_war_ship_sum}")
        ship = False
        break
    cmd = cmd.split()
    if cmd[0] == "Fire":
        if 0 <= int(cmd[1]) < len(man_o_war_status):
            man_o_war_status[int(cmd[1])] -= int(cmd[2])
            if man_o_war_status[int(cmd[1])] <= 0:
                print("You won! The enemy ship has sunken.")
                ship = False
                break
    elif cmd[0] == "Defend":
        if 0 <= int(cmd[1]) < len(pirate_status) and 0 < int(cmd[2]) < len(pirate_status) and int(cmd[1]) <= int(cmd[2]):
            for section_index in range(int(cmd[1]), int(cmd[2]) + 1):
                pirate_status[section_index] -= int(cmd[3])
                if pirate_status[section_index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    ship = False
                    break
    elif cmd[0] == "Repair":
        if 0 <= int(cmd[1]) < len(pirate_status):
            pirate_status[int(cmd[1])] += int(cmd[2])
            if pirate_status[int(cmd[1])] > max_health_section:
                pirate_status[int(cmd[1])] = max_health_section
    elif cmd[0] == "Status":
        for item in pirate_status:
            if item < max_health_section * is_for_repair:
                pirate_for_repair_sections += 1
        print(f"{pirate_for_repair_sections} sections need repair.")
