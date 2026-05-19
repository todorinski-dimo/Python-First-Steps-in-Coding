lst = input().split()
out = []
for _ in range(len(lst)):
    out.append(lst.pop())
print(" ".join(out))
