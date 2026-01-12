pprice = 5.8
mprice = 7.2
cprice = 1.2

pq = int(input())
mq = int(input())
cq = int(input())
discountq = int(input())
discount = discountq / 100

total = pq * pprice + mq * mprice + cq * cprice
totaldiscount = total * discount
totalf = total - totaldiscount

print(totalf)