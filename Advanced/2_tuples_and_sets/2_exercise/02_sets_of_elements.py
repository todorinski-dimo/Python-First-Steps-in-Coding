n, m= [int(x) for x in input().split()]
# nm = n + m
# n_set = set()
# m_set = set()

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

# for i in range(nm):
#     if i < n:
#         n_set.add(int(input()))
#     else:
#         m_set.add(int(input()))
result = n_set & m_set
# for item in result:
#     print(item)
print(*result, sep="\n")