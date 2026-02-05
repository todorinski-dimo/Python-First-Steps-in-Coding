# https://alpha.judge.softuni.org/contests/06-programming-fundamentals-mid-exam-retake/1773/practice#1
# score 100

days_for_plunder = int(input())
daily_plunder = int(input())
target_plunder = int(input())
total_plunder = 0
bonus_at_day = 3
bonus_at_bonus_day = 0.5  # for daily plunder
battle_at_day = 5
loss_at_battle_day = 0.3  # for total plunder

for day in range(1, days_for_plunder + 1):
    total_plunder += daily_plunder
    if day % bonus_at_day == 0:
        total_plunder += bonus_at_bonus_day * daily_plunder
    if day % battle_at_day == 0:
        total_plunder *= 1 - loss_at_battle_day

if total_plunder >= target_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(total_plunder/target_plunder)*100:.2f}% of the plunder.")
