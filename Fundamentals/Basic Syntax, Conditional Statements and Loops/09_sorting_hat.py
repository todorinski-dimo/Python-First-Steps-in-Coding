while True:
    new_name = input()
    if new_name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif new_name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif len(new_name) < 5:
        print(f"{new_name} goes to Gryffindor.")
    elif len(new_name) == 5:
        print(f"{new_name} goes to Slytherin.")
    elif len(new_name) == 6:
        print(f"{new_name} goes to Ravenclaw.")
    else:
        print(f"{new_name} goes to Hufflepuff.")
