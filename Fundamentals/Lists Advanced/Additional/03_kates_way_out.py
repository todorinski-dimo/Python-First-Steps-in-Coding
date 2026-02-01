def where_is_the_exit(mz_2d: list) -> list:
    exits = []
    for row in range(len(mz_2d)):
        if row == 0 or row == len(mz_2d) - 1:
            for pos in range(len(mz_2d[row])):
                if mz_2d[row][pos] == " ":
                    exits.append([row, pos])
        elif mz_2d[row][0] == " ":
            exits.append([row, 0])
        elif mz_2d[row][-1] == " ":
            exits.append([row, -1])
    return exits


def where_is_player(mz_2d: list) -> list:
    player = []
    for row in range(len(mz_2d)):
        for pos in range(len(mz_2d[row])):
            if mz_2d[row][pos] == "k":
                player = [row, pos]
    return player


def player_moves(mz_2d: list, plr: list, ext: list) -> str:
    if len(ext) == 0:
        return "Kate cannot get out"
    move = 0
    row = plr[0]
    pos = plr[1]
    possible_positions = [[row, pos]]
    next_possible_positions = []
    exit_moves = []
    while True:
        for i in range(len(possible_positions)):
            row = possible_positions[i][0]
            pos = possible_positions[i][1]
            if pos + 1 < len(mz_2d[row]):
                if mz_2d[row][pos + 1] == " ":
                    mz_2d[row][pos + 1] = move
                    next_possible_positions.append([row, pos + 1])
            if row + 1 < len(mz_2d):
                if mz_2d[row + 1][pos] == " ":
                    mz_2d[row + 1][pos] = move
                    next_possible_positions.append([row + 1, pos])
            if pos - 1 < len(mz_2d[row]):
                if mz_2d[row][pos - 1] == " ":
                    mz_2d[row][pos - 1] = move
                    next_possible_positions.append([row, pos - 1])
            if row - 1 < len(mz_2d):
                if mz_2d[row - 1][pos] == " ":
                    mz_2d[row - 1][pos] = move
                    next_possible_positions.append([row - 1, pos])
        possible_positions = next_possible_positions
        next_possible_positions = []
        move += 1
        if len(possible_positions) == 0:
            for i in range(len(mz_2d)):
                print(mz_2d[i])
            break

    for h in range(len(ext)):
        if mz_2d[ext[h][0]][ext[h][1]] != " " and mz_2d[ext[h][0]][ext[h][1]] != "#":
            exit_moves.append(mz_2d[ext[h][0]][ext[h][1]])

    if len(exit_moves) == 0:
        return "Kate cannot get out"

    move = max(exit_moves)
    return f"Kate got out in {move + 2} moves"


rows = int(input())
maze = []
for _ in range(rows):
    maze.append(list(input()))
# print(where_is_the_exit(maze))
# print(where_is_player(maze))
print(player_moves(maze, where_is_player(maze), where_is_the_exit(maze)))
