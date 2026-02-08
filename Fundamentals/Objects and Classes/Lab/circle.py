class Circle:
    __pi = 3.14

    def __init__(self, circle_diameter):
        self.circle_diameter = circle_diameter
        self.circle_radius = circle_diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.circle_diameter

    def calculate_area(self):
        return Circle.__pi * self.circle_radius ** 2

    def calculate_area_of_sector(self, angle_sector):
        return (angle_sector / 360) * Circle.__pi * self.circle_radius ** 2

circle1 = Circle(10)
angle = 5

print(f"{circle1.calculate_circumference():.2f}")
print(f"{circle1.calculate_area():.2f}")
print(f"{circle1.calculate_area_of_sector(angle):.2f}")

