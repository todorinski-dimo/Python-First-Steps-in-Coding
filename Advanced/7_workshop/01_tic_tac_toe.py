def check_for_winner(matrix: list, sign: str) -> bool:
    # Check for row
    for m_row in matrix:
        if m_row.count(sign) == 3:
            return True

    # Check for col
    for col_idx in range(3):
        counter = 0
        for row_idx in range(3):
            if matrix[row_idx][col_idx] == sign:
                counter +=1
        if counter == 3:
            return True

    # Check for primary diagonal
    counter = 0
    for idx in range(3):
        if matrix[idx][idx] == sign:
            counter += 1
    if counter == 3:
        return True

    # Check for secondary diagonal
    counter = 0
    for index in range(3):
        if matrix[index][3 - index - 1] == sign:
            counter +=1
    if counter == 3:
        return True

    # No winner
    return False

def check_for_free_positions(matrix: list) -> str:
    key = []
    for f_row in range(3):
        for f_col in range(3):
            if matrix[f_row][f_col] == " ":
                f_list =[f_row,f_col]
                key.extend([str(key) for key, value in mapper.items() if value == tuple(f_list)])
    f_str = ", ".join(key)
    return f_str

# Creating the board.
board = [[" ", " ", " "] for _ in range(3)]

# Defining coordinates in the board matrix for board position's
mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}

# Taking player names. Must be different
player_one_name = input("Enter First Player Name: ")
player_one_name = player_one_name[0].upper()+player_one_name[1:].lower()
player_two_name = input("Enter Second Player Name: ")
player_two_name = player_two_name[0].upper()+player_two_name[1:].lower()
while player_two_name == player_one_name:
    player_two_name = input("Name is used by the First Player. Enter new name:")
    player_two_name = player_two_name[0].upper() + player_two_name[1:].lower()

# Taking player signs. Making sure they are valid.
player_one_sign = ""
player_two_sign = ""
while player_one_sign not in ["X", "O"]:
    player_one_sign = input(f"{player_one_name} enter 'X' or 'O' for your sign on the board:").upper()
    if player_one_sign not in ["X", "O"]:
        print(f"{player_one_name}, you've entered invalid sign.")
    player_two_sign = "O" if player_one_sign == "X" else "X"

# Printing board numeration and instructions for the players.
print("This is how the positions are numbered.")
print("Use them to choose where to put your sign.")
[print(f"| {i} | {i+1} | {i+2} |") for i in range(1,10,3)]
print()

# Counting turns.
turn = 1

# Game starts. Players take turns and put their signs on the board.
print(f"{player_one_name} is first to choose position on the board.")

while True:
    # Checks if board is filled. If there was winner before that, cycle would have stopped
    if turn == 10:
        print("Board is full. Noone wins.")
        break

    # Defining current player to play.
    current_player, current_sign = (player_one_name, player_one_sign) if turn % 2 == 1 \
        else (player_two_name, player_two_sign)

    # Player selecting the position on the board
    try:
        position = int(input(f"{current_player}({current_sign}) enter a positon. Free positions: {check_for_free_positions(board)}: "))
    except ValueError:
        print("Please enter an integer.")
        # Input is not integer - restarts to input prompt
        continue
    if position < 1 or position > 9:
        print("Please enter a valid position - from 1 to 9.")
        # Input is not in range - restart to input prompt
        continue

    # Checking for open position and saving players selection
    row, col = mapper[position]
    if board[row][col] != " ":
        print("This position is already used.")
        continue
    else:
        board[row][col] = current_sign
        for row in board:
            print(f" | {' | '.join(row)} | ")

    # Checking for winner
    if turn > 4 and check_for_winner(board, current_sign):
        print(f"{current_player} wins.")
        break

    #Game continues if game is not won or board is filled
    turn += 1
    print()