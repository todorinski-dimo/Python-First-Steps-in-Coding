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

for i in range(len(battlefield)):
    print(battlefield[i])
print(hits)

for i in range(len(hits)):
    x = int(hits[i][0])
    y = int(hits[i][1])
    print(battlefield[x, y])

for i in range(len(battlefield)):
    print(battlefield[i])
print(hits)