protectorp = 1.5
paintp = 14.5
painttp = 5.0
abag = 0.4

protectorq = int(input())
paintq = int(input())
painttq = int(input())
workh = int(input())

aprotector = (protectorq + 2) * protectorp
apaint = paintq * 1.1 *paintp
apaintt = painttq * painttp

amaterials = aprotector + apaint + apaintt + abag
awork = amaterials * 0.3 * workh
total = amaterials + awork

print(total)