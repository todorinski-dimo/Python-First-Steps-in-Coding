from random import randrange
from time import sleep
import os


def loading_screen(stat: int) -> str:
    """takes an integer; returns loading bar message in 10%steps"""
    if stat == 10:
        return "100% [%%%%%%%%%%]\nComplete!        "
    if 0 <= stat < 10:
        return f"{stat * 10}% [{'%' * stat}{'.' * (10 - stat)}]\nStill loading..."


# def cls():
#     os.system('cls' if os.name == 'nt' else 'clear')


# instead of clearing the console with "cls", as it make the console flicker, we enable ANSI processing
os.system("")
for status in range(0, 11):
    # using \r in the print string moves the cursor back to the beginning of the console and combined with
    # not moving to new line, the next print will overwrite the printed old text
    print()
    print(f"\r{loading_screen(status)}", end="")
    sleep(randrange(1, 2))
    # cls()
    # using ANSI '\033[3A' to be executed it moves the cursor 3 lines up (in this case - change # in '\033[#A'
    # to move the cursor diff number of lines
    print('\033[3A')
print()
print()
print()
