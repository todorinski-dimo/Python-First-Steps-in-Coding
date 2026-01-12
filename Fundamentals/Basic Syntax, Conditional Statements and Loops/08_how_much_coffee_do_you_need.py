numb_coffees = 0
while True:
    event = input()
    if event == "END":
        break
    elif event == "cat" or event == "dog" or event == "coding" or event == "movie":
        numb_coffees += 1
    elif event == "CAT" or event == "DOG" or event == "CODING" or event == "MOVIE":
        numb_coffees += 2
if numb_coffees > 5:
    print("You need extra sleep")
else:
    print(numb_coffees)