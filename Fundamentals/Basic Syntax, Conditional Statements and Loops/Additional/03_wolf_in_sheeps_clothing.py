string = input()
string_list = string.split(", ")
wolf_pos = 0
for pos in range(len(string_list)-1, -1, -1):
    if pos == len(string_list) - 1 and string_list[pos] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif string_list[pos] == "wolf":
        print(f"Oi! Sheep number {len(string_list) - pos - 1}! You are about to be eaten by a wolf!")
        break
#wolf, sheep, sheep, sheep, sheep, sheep
#sheep, sheep, wolf
#sheep, sheep, sheep, sheep, wolf, sheep, sheep, sheep