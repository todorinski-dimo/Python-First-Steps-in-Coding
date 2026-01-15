deposit = float(input())
months = int(input())
ypr = float(input())
yprr = ypr / 100
total = deposit + months * deposit * yprr / 12

print(total)