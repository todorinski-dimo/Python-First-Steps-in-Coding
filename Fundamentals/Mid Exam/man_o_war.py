# https://alpha.judge.softuni.org/contests/06-programming-fundamentals-mid-exam-retake/1773/practice#3
# score 100

pirate_ship_status = [int(item) for item in input().split(">")]
wars_ship_status = [int(item) for item in input().split(">")]
section_max_health = int(input())

idx = 0
idx_end = 0
damage = 0
sections_for_repair = []
cycle_status = True
sunken = False

while cycle_status:
    cmd = input().split()
    if cmd[0] == "Retire":
        cycle_status = False
        break
    elif cmd[0] == "Fire":
        idx = int(cmd[1])
        damage = int(cmd[2])
        if -1 < idx < len(wars_ship_status):
            wars_ship_status[idx] -= damage
            if wars_ship_status[idx] <= 0:
                cycle_status = False
                sunken = True
                print("You won! The enemy ship has sunken.")
                break
    elif cmd[0] == "Defend":
        idx = int(cmd[1])
        idx_end = int(cmd[2])
        damage = int(cmd[3])
        if -1 < idx < len(pirate_ship_status) and -1 < idx_end < len(pirate_ship_status):
            for ix in range(idx, idx_end + 1):
                pirate_ship_status[ix] -= damage
                if pirate_ship_status[ix] <= 0:
                    cycle_status = False
                    sunken = True
                    print("You lost! The pirate ship has sunken.")
                    break
    elif cmd[0] == "Repair":
        idx = int(cmd[1])
        damage = int(cmd[2])
        if -1 < idx < len(pirate_ship_status):
            pirate_ship_status[idx] += damage
            if pirate_ship_status[idx] > section_max_health:
                pirate_ship_status[idx] = section_max_health
    elif cmd[0] == "Status":
        sections_for_repair = list(filter(lambda section: section < 0.2 * section_max_health, pirate_ship_status))
        print(f"{len(sections_for_repair)} sections need repair.")

if not sunken:
    print(f"Pirate ship status: {sum(pirate_ship_status)}")
    print(f"Warship status: {sum(wars_ship_status)}")


