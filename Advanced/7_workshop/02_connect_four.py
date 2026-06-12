class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def print_matrix(ma):
    for line in ma:
        print(line)


def validate_column_choice(col, max_index):
    if not (0 <= col < max_index):
        raise InvalidColumnError


def place_player_choice(ma, c, player_num):
    for r in range(len(ma) - 1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player_num
            return r, c
    raise FullColumnError


def is_player_num(ma, r, c, player_num):
    if r < 0 or c < 0 or r >= len(ma) or c >= len(ma[0]):
        return False
    return ma[r][c] == player_num


def is_vertical_win(ma, r, c, player_num, slots):
    return all(is_player_num(ma, r + idx, c, player_num) for idx in range(slots))


def is_horizontal_win(ma, r, c, player_num, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r, c + idx, player_num):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r, c - idx, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def is_right_diagonal_win(ma, r, c, player_num, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, player_num):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def is_left_diagonal_win(ma, r, c, player_num, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, player_num):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, player_num):
            filled += 1
        else:
            break

    return filled >= slots


def is_winner(ma, r, c, player_num, slots=4):
    return any([
        is_vertical_win(ma, r, c, player_num, slots),
        is_horizontal_win(ma, r, c, player_num, slots),
        is_right_diagonal_win(ma, r, c, player_num, slots),
        is_left_diagonal_win(ma, r, c, player_num, slots)
    ])


rows_count = 6
cols_count = 7

matrix = create_matrix(rows_count, cols_count)
print_matrix(matrix)

player = 1
counter = 0

while True:
    try:
        column_num = int(input(f"Player {player}, please choose a column: ")) - 1
        validate_column_choice(column_num, cols_count - 1)
        row, col = place_player_choice(matrix, column_num, player)
        print_matrix(matrix)

        if is_winner(matrix, row, col, player):
            print(f"The winner is Player {player}")
            break

        counter += 1
        if rows_count * cols_count == counter:
            print("The game is draw!")
            break

        player = 2 if player == 1 else 1

    except FullColumnError:
        print("This column is full. Please, select another!")
        continue
    except InvalidColumnError:
        print(f"Select a valid number (between 1 and {cols_count})!")
        continue
    except ValueError:
        print("This is not a digit! Please select a valid column number!")
        continue