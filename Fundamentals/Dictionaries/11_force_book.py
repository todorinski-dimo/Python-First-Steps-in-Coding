forces = {}
force_available = False
user_available = False


while True:
    cmd = input()
    if "|" in cmd:
        cmd = cmd.split(" | ")
        force_side = cmd[0]
        force_user = cmd[1]
        if force_user not in forces.keys():
            forces[force_user] = force_side
    elif "->" in cmd:
        cmd = cmd.split(" -> ")
        force_side = cmd[1]
        force_user = cmd[0]
        forces[force_user] = force_side
        print(f"{force_user} joins the {force_side} side!")
    elif cmd == "Lumpawaroo":
        break
print(forces)