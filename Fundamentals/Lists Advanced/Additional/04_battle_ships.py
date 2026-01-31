rows = int(input())
battlefield = []

for _ in range(rows):
    battlefield.append([int(item) for item in input().split()])
hits = input().split()
for i in range(len(hits)):
    hits[i] = hits[i].split("-")

for i in range(len(hits)):
    for j in range(len(hits[i])):
        hits[i][j] = int(hits[i][j])

sink_ships = 0

# for i in range(len(battlefield)):
#     print(battlefield[i])
# print(hits)

for i in range(len(hits)):
    if battlefield[hits[i][0]][hits[i][1]] > 0:
        battlefield[hits[i][0]][hits[i][1]] -= 1
        if battlefield[hits[i][0]][hits[i][1]] == 0:
            sink_ships += 1


# for i in range(len(battlefield)):
#     print(battlefield[i])
# print(hits)

print(sink_ships)
