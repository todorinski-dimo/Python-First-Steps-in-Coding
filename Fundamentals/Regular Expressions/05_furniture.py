import re

# cmd = input()
# buff = []
# cost = 0
# regex = r">>([a-z]+)<<(\d+\.?\d*)!(\d+)"
# while cmd != "Purchase":
#     check = re.search(regex, cmd, re.IGNORECASE)
#     if check:
#         furn, price, qty = check.groups()
#         buff.append(furn)
#         cost += float(price)*int(qty)
#     cmd = input()
# print("Bought furniture:")
# for item in buff:
#     print(item)
# print(f"Total money spend: {cost:.2f}")

import re

cmd = input()
buff = []
cost = 0
regex = r">>([a-zA-Z]+)<<(\d+\.?\d+?)!(\d+)"
while cmd!="Purchase":
    check = re.findall(regex, cmd)
    if check:
        buff += check
    cmd = input()
print("Bought furniture:")
for item in buff:
    print(item[0])
    cost += float(item[1])*int(item[2])
print(f"Total money spend: {cost:.2f}")