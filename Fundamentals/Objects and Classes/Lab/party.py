class Party:
    def __init__(self):
        self.people = []


party1 = Party()

while True:
    names = input()
    if names == "End":
        break
    else:
        party1.people.append(names)

print(f"Going: {', '.join(party1.people)}")
print(f"Total: {len(party1.people)}")
