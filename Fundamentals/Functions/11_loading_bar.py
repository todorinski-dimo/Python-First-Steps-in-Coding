def loading_screen(stat: int) -> str:
    """takes an integer; returns loading bar message in 10%steps"""
    if stat == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    if 0 <= stat < 100:
        return f"{stat}% [{'%' * (stat // 10)}{'.' * (10 - (stat // 10))}]\nStill loading..."


loading_stat = int(input())
print(loading_screen(loading_stat))
