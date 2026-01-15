import random

very_close_check = 3
close_check = 10
near_check = 20
way_off = 50

print("Try to guess the number the computer have in mind.")
print("== First choose difficulty. ==")
print("== Enter \"easy\" for number between 1 and 10. ==")
print("== Enter \"medium\" for number between 1 and 50. ==")
print("== Enter \"hard\" for number between 1 and 100. ==")
print("")

difficulty = input("Enter difficulty: ")
if difficulty == "easy":
    range_end = 10
    print(f"You selected an easy game. Try to guess the number in range from 1 to {range_end}.")
elif difficulty == "medium":
    range_end = 50
    print(f"You selected a medium game. Try to guess the number in range from 1 to {range_end}.")
elif difficulty == "hard":
    range_end = 100
    print(f"You selected a hard game. Try to guess the number in range from 1 to {range_end}.")
else:
    range_end = 1000
    print(f"I see... You wanna play very hard. Range is from 1 to 1000.")

random_number = random.randint(1, range_end)

#print(f"For testing purposes computer number is {random_number}.")

while True:
    print("")
    print(f"Enter a number from 1 to {range_end}: ", end="")
    input_number = input()
    if not input_number.isdigit():
        print("Try again with an integer.")
        continue
    if int(input_number) == random_number:
        print("BINGO! You hit the number.")
        break
    else:
        if difficulty == "easy":
            if int(input_number) > 10:
                print("The number you tried with is out of the range. Try again.")
            elif random_number > int(input_number) > random_number - very_close_check:
                print(f"You are very close ({very_close_check}). Try with higher number.")
            elif random_number < int(input_number) < random_number + very_close_check:
                print(f"You are very close ({very_close_check}). Try with lower number.")
        elif difficulty == "medium":
            if int(input_number) > 50:
                print("The number you tried with is out of the range. Try again.")
            elif random_number + very_close_check > int(input_number) > random_number - very_close_check:
                print(f"You are very close ({very_close_check}).")
            elif random_number > int(input_number) > random_number - close_check:
                print(f"You are close ({close_check}). Try with higher number.")
            elif random_number < int(input_number) < random_number + close_check:
                print(f"You are close ({close_check}). Try with lower number.")

        elif difficulty == "hard":
            if int(input_number) > 100:
                print("The number you tried with is out of the range. Try again.")
            elif random_number + very_close_check > int(input_number) > random_number - very_close_check:
                print(f"You are very close ({very_close_check}).")
            elif random_number + close_check > int(input_number) > random_number - close_check:
                print(f"You are close ({close_check}).")
            elif random_number > int(input_number) > random_number - near_check:
                print(f"You are near ({near_check}). Try with higher number.")
            elif random_number < int(input_number) < random_number + near_check:
                print(f"You are near ({near_check}). Try with higher number.")
        else:
            if int(input_number) > 1000:
                print("The number you tried with is out of the range. Try again.")
            elif random_number + way_off > int(input_number) > random_number - way_off:
                print(f"You are way off ({way_off}).")

print("")
print("Thanks for playing.")
print("That was all, Folks.")
