days = int(input())
available_food = float(input())

total_eaten_food = 0.0
total_dog_eaten_food = 0.0
total_cat_eaten_food = 0.0
biscuits = 0.0
day_number = 0

for day_number in range(days):
    dog_food_eaten = float(input())
    cat_food_eaten = float(input())
    total_dog_eaten_food += dog_food_eaten
    total_cat_eaten_food += cat_food_eaten
    if (day_number+1) % 3 == 0:
        biscuits += (dog_food_eaten + cat_food_eaten) * 0.1

total_eaten_food = total_dog_eaten_food + total_cat_eaten_food
percent_total_eaten_food = total_eaten_food / available_food * 100
percent_dog_eaten_food = total_dog_eaten_food / total_eaten_food * 100
percent_cat_eaten_food = total_cat_eaten_food / total_eaten_food * 100
biscuits = round(biscuits)

print(f"Total eaten biscuits: {biscuits}gr.")
print(f"{percent_total_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_eaten_food:.2f}% eaten from the dog.")
print(f"{percent_cat_eaten_food:.2f}% eaten from the cat.")