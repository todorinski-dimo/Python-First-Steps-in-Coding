from collections import deque

materials = [int(item) for item in input().split()]
magic = deque(int(item) for item in input().split())

adding_material = 15

magic_for_toys = {
    150:"Doll",
    250:"Wooden train",
    300:"Teddy bear",
    400:"Bicycle"
    }

created_toys = {}


while materials and magic:
    ttl_magic = materials[-1] * magic[0]
    if ttl_magic in magic_for_toys:
        new_toy = magic_for_toys[ttl_magic]
        created_toys[new_toy] = created_toys.get(new_toy, 0) + 1
        materials.pop()
        magic.popleft()
    elif ttl_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif ttl_magic > 0:
        magic.popleft()
        materials[-1] += adding_material
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic[0] == 0:
            magic.popleft()

if ("Doll" in created_toys and "Wooden train" in created_toys)\
    or ("Teddy bear" in created_toys and "Bicycle" in created_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")

for key, value in sorted(created_toys.items()):
    print(f"{key}: {value}")
