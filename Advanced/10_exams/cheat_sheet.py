# operators = {
#     "a": lambda x, y: x + y,
#     "s": lambda x, y: x - y,
#     "d": lambda x, y: x / y if y != 0 else x,
#     "m": lambda x, y: x * y
# }
# ----------------
# possible_moves = {
#     "down": (1, 0),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "left": (0, -1),
# }
# n_row, n_col = player[0] + possible_moves[input()][0], player[1] + possible_moves[input()][1]
# ----------------
# commands_map = {
#     "up": lambda r, c: (r-1, c) if r-1 >= 0 else (r, c),
#     "down": lambda r, c: (r+1, c) if r+1 < n else (r, c),
#     "left": lambda r, c: (r, c-1) if c-1 >= 0 else (r, c),
#     "right": lambda r, c: (r, c+1) if c+1 < n else (r, c)
# }
# new_p_row, new_p_col = commands_map[command](player_row, player_col)
# commands_map = {
#     "up": lambda r, c: ((r-1) % n, c % n),
#     "down": lambda r, c: ((r+1) % n, c % n),
#     "left": lambda r, c: (r % n, (c-1) % n),
#     "right": lambda r, c: (r % n, (c+1) % n)
# }
# bee = []
# bee = commands_map[command](bee[0], bee[1])
# ----------------
# knight_moves = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]
# expld = ((-1, 0), (1, 0), (0, -1), (0, 1))
# ----------------
# for length_name, length_length in sorted(length.items(), key=lambda item: (item[1], item[0])):
#     pass
# a_room = {k: v for k, v in sorted(rooms.items(), key=lambda item: (item[1], item[0]))}
# ----------------
# snake:
# for col in range(cols):
#     if row % 2 == 0:
#         matrix[row][col] = txt[0]
#     else:
#         matrix[row][-1 - col] = txt[0]
# ----------------
# rows, cols = map(int, input().split())
# matrix = [[x for x in input().split()]for row in range(rows)]
# rows, cols = map(int, input().split())
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# ---------------
# diagonals
# square = int(input())
# matrix = [[int(x) for x in input().split(",")] for _ in range(square)]
#
# primary_diagonal = [matrix[i][i] for i in range(square)]
# secondary_diagonal = [matrix[i][-1 - i] for i in range(square)]
# ---------------
# deque
# strength = list(map(int, input().split()))
# accuracy = deque(list(map(int, input().split())))