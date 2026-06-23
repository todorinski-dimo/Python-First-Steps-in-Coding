def sort_games(*g_type, **g_release):
    sg_type = sorted(g_type, key=lambda x: x[0])
    sg_release_console = {k:v for k,v in sorted(g_release.items(), key=lambda x: x[0])}
    sg_release_pc = {k:v for k,v in sorted(g_release.items(), key=lambda x: x[0], reverse=True)}
    console_games = []
    pc_games = []

    for date, name in sg_release_console.items():
        for item in sg_type:
            if item[0] == "console":
                if item[1] == name:
                    console_games.append(f">>>{date[:-4]}: {name}")
    for date, name in sg_release_pc.items():
        for item in sg_type:
            if item[0] == "pc":
                if item[1] == name:
                    pc_games.append(f"<<<{date[:-4]}: {name}")

    result =[]


    if console_games:
        result.append("Console Games:")
        for item in console_games:
            result.append(item)
    if pc_games:
        result.append("PC Games:")
        for item in pc_games:
            result.append(item)

    resul_result = "\n".join(result)

    return resul_result


print(sort_games(
    ("console", "Echo Dive"),
    ("pc", "Quantum Drift"),
    June_22_2025_001="Quantum Drift",
    March_15_2025_002="Echo Dive",
))
print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))
print(sort_games(
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("console", "Blade Echo"),
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
))
print(sort_games(
    ("pc", "Iron Comet"),
    ("pc", "Neon Skyline"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))

AssertionError: (
'Cons[20 chars]_15_2025: Echo Dive\nPC Games:\n>>>June_22_2025: Quantum Drift' !=
'Cons[20 chars]_15_2025: Echo Dive\nPC Games:\n<<<June_22_2025: Quantum Drift')