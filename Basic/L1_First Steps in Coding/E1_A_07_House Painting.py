side_x = float(input())
side_y = float(input())
side_h = float(input())

area_frontwall = (side_x * side_x) - (1.2 * 2)
area_backwall = side_x * side_x
area_sidewalls = 2 * ((side_x * side_y) - (1.5 * 1.5))
area_toproofs = 2 * (side_x * side_y)
area_frontroofs = 2 * ((side_x * side_h) / 2)

paint_siderate = 3.4
paint_roofrate = 4.3

print(f"{(area_backwall + area_frontwall + area_sidewalls)/paint_siderate:.02f}")
print(f"{(area_toproofs + area_frontroofs)/paint_roofrate:.02f}")
