qgodi_price = float(input())
banana_quantity = float(input())
oranges_quantity = float(input())
malini_quantity = float(input())
qgodi_quantity = float(input())

malini_price = 0.5 * qgodi_price
banana_price = 0.2 * malini_price
oranges_price = 0.6 * malini_price


total_cost = banana_price * banana_quantity + oranges_price * oranges_quantity + qgodi_price * qgodi_quantity + malini_price * malini_quantity
print(f"{total_cost:.2f}")