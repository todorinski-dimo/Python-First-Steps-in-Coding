# https://alpha.judge.softuni.org/contests/05-programming-fundamentals-mid-exam/2028/practice#2
# score 100

health = 100
coins = 0
killed = False
dungeons = [item for item in input().split("|")]

for room in range(len(dungeons)):
    cmd = dungeons[room].split()
    if cmd[0] == "potion":
        if health + int(cmd[1]) >= 100:
            heal = 100 - health
            health = 100
        else:
            heal = int(cmd[1])
            health += int(cmd[1])
        print(f"You healed for {heal} hp.")
        print(f"Current health: {health} hp.")
    elif cmd[0] == "chest":
        coins += int(cmd[1])
        print(f"You found {cmd[1]} bitcoins.")
    else:
        health -= int(cmd[1])
        if health <= 0:
            print(f"You died! Killed by {cmd[0]}.")
            print(f"Best room: {room + 1}")
            killed = True
            break
        else:
            print(f"You slayed {cmd[0]}.")

if not killed:
    print("You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")

