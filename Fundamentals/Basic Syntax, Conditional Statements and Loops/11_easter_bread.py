number_of_loaves = 0
colored_eggs = 0

budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price_per_loaf = 0.25 * 1.25 * flour_price
loaf_price = flour_price + eggs_price + milk_price_per_loaf

while budget > loaf_price:
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs = colored_eggs - (number_of_loaves - 2)
    budget -= loaf_price

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}"
f"BGN left.")
