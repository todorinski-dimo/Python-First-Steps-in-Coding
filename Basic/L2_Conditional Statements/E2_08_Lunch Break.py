from math import ceil
film_name = input()
film_len = int(input())
rest_len = int(input())

len_for_film = rest_len - (rest_len * 3) / 8

diff = ceil(abs(film_len - len_for_film))

if len_for_film - film_len >= 0:
    print(f"You have enough time to watch {film_name} and left with {diff} minutes free time.")
else:
    print(f"You don't have enough time to watch {film_name}, you need {diff} more minutes.")