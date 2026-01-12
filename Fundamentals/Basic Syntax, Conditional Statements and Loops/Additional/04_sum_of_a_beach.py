beach = input()
beach_lower = beach.lower()
counter = 0
for pos in range(len(beach_lower)):
    if beach_lower[pos:pos+5] == "water":
        counter += 1
    if beach_lower[pos:pos+4] == "sand" or beach_lower[pos:pos+4] == "fish":
        counter += 1
    if beach_lower[pos:pos+3] == "sun":
        counter += 1
print(counter)

