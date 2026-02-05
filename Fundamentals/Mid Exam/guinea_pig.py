# https://alpha.judge.softuni.org/contests/04-programming-fundamentals-mid-exam/2031/practice#1
# score 100

food = float(input())*1000
hay = float(input())*1000
cover = float(input())*1000
weight = float(input())*1000

days = 30
puppy_eats = 600
puppy_hays = 0.05

for day in range(1, days + 1):
    if day % 2 == 0:
        food -= puppy_eats
        hay -= puppy_hays * food
    if day % 3 == 0:
        cover -= weight / 3

if food <= 0 or hay <= 0 or cover <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.")

