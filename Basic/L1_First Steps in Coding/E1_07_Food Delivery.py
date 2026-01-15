chicken = int(input())
fish = int(input())
vegan = int(input())

chicken_price = 10.35
fish_price = 12.40
vegan_price = 8.15

total_before_desert = chicken * chicken_price + fish_price * fish + vegan_price * vegan
total = total_before_desert * 1.20 + 2.50

print(f"{total:.2f}")


