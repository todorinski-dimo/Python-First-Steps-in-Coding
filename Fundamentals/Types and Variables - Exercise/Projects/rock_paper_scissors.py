import random

score_computer_wins = 0
score_player_wins = 0
score_draws = 0
options = ["Rock", "Paper", "Scissors"]

print("This is the Rock-Paper-Scissors game.")
print("Try to beat the computer.")


while True:
    computer_choice_int = random.randint(1, 3)
    computer_choice = options[computer_choice_int - 1]
    print(f"For testing purposes computer has chosen \"{computer_choice}\"")
    print("")
    print("Computer has chosen a stance. What is yours?")
    player_input = input("Enter [R]ock, [P]paper or [S]scissors: ")
    if player_input not in ["r", "p", "s", "R", "P", "S", "rock", "paper", "scissors", "Rock", "Paper", "Scissors"]:
        print("")
        print("Try again.")
    elif (player_input in ["r", "R", "rock", "Rock"] and computer_choice == "Rock") \
            or (player_input in ["p", "P", "paper", "Paper"] and computer_choice == "Paper") \
            or (player_input in ["s", "S", "scissors", "Scissors"] and computer_choice == "Scissors"):
        print("")
        print(f"Draw. Computer and you chose {computer_choice}.")
        score_draws += 1
    elif (player_input in ["r", "R", "rock", "Rock"] and computer_choice == "Scissors") \
            or (player_input in ["p", "P", "paper", "Paper"] and computer_choice == "Rock") \
            or (player_input in ["s", "S", "scissors", "Scissors"] and computer_choice == "Paper"):
        print("")
        print(f"You WIN! Computer chose {computer_choice}.")
        score_player_wins += 1
    else:
        print("")
        print(f"You Lose! Computer chose {computer_choice}.")
        score_computer_wins += 1
    print(f"Score: Wins - {score_player_wins}, Losses - {score_computer_wins}, Draws - {score_draws}.")
    print("")
    print("Do you want to continue? [Y]es or [N]o: ", end="")
    if input() in ["Yes", "yes", "Y", "y"]:
        continue
    else:
        break
