deck = input().split()
shuffles = int(input())

middle_item = int(len(deck)/2)
new_deck = []

for _ in range(0, shuffles):
    deck_half_a = deck[:middle_item]
    deck_half_b = deck[middle_item:]
    for item in range(0, middle_item):
        new_deck.append(deck_half_a[item])
        new_deck.append(deck_half_b[item])
    deck = new_deck

print(deck)
