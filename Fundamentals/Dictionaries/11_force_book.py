forces = {}

while True:
    cmd = input()
    if "|" in cmd:
        cmd = cmd.split(" | ")
        force_available = False
        user_available = False
        force_side = cmd[0]
        force_user = cmd[1]
        for value in forces.values():
            if force_user in value:
                user_available = True
        for key in forces.keys():
            if force_side in key:
                force_available = True
        if not user_available and not force_available:
            forces[force_side] = [force_user]
        elif not user_available and force_available:
            forces[force_side].append(force_user)
    elif "->" in cmd:
        cmd = cmd.split(" -> ")
        force_available = False
        user_available = False
        force_side = cmd[1]
        force_user = cmd[0]
        for value in forces.values():
            if force_user in value:
                user_available = True
        for key in forces.keys():
            if force_side in key:
                force_available = True
        if not user_available and not force_available:
            forces[force_side] = [force_user]
            print(f"{force_user} joins the {force_side} side!")
        elif not user_available and force_available:
            forces[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        if user_available:
            for side, users in forces.items():
                if force_user in users:
                    users.remove(force_user)
            if force_side not in forces.keys():
                forces[force_side] = []
            forces[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
    elif cmd == "Lumpawaroo":
        break

for side, users in forces.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")