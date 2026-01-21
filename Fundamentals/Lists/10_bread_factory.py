init_energy = 100
curr_energy = 100
order_energy = 30
rest_order_energy = 50
init_coins = 100
curr_coins = 100
event_pos = 0
prem_closed = False

events_list = input().split("|")
events_list_mod = []

for event in range(len(events_list)):
    events_list_mod.append(events_list[event].split("-"))

while event_pos < len(events_list_mod):
    if events_list_mod[event_pos][0] == "rest":
        if int(events_list_mod[event_pos][1]) + curr_energy > init_energy:
            print(f"You gained {init_energy - curr_energy} energy.")
            curr_energy = 100
        else:
            print(f" You gained {int(events_list_mod[event_pos][1])} energy.")
            curr_energy += int(events_list_mod[event_pos][1])
        print(f"Current energy: {curr_energy}.")
    elif events_list_mod[event_pos][0] == "order":
        if curr_energy >= order_energy:
            curr_energy -= order_energy
            curr_coins += int(events_list_mod[event_pos][1])
            print(f"You earned {int(events_list_mod[event_pos][1])} coins.")
        else:
            print("You had to rest!")
            curr_energy += rest_order_energy
            if curr_energy > 100:
                curr_energy = 100
    else:
        if curr_coins - int(events_list_mod[event_pos][1]) < 0:
            print(f"Closed! Cannot afford {events_list_mod[event_pos][0]}.")
            prem_closed = True
            break
        else:
            print(f"You bought {events_list_mod[event_pos][0]}.")
            curr_coins -= int(events_list_mod[event_pos][1])

    event_pos += 1

if not prem_closed:
    print("Day completed!")
    print(f"Coins: {curr_coins}")
    print(f"Energy: {curr_energy}")
