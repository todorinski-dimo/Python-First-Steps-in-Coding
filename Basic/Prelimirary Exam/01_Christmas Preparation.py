paper_price = 5.8
cloth_price = 7.2
glue_price = 1.2

paper_quantity = int(input())
cloth_quantity = int(input())
glue_quantity = float(input())
discount = int(input())

percent_discount = 1 - (discount/100)

total = percent_discount * (paper_quantity * paper_price + cloth_quantity * cloth_price + glue_quantity * glue_price)

print(f"{total:.3f}")