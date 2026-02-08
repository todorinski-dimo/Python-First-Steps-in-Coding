class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, animal_species, animal_name):
        if animal_species == "mammal":
            self.mammals.append(animal_name)
        elif animal_species == "fish":
            self.fishes.append(animal_name)
        elif animal_species == "bird":
            self.birds.append(animal_name)
        Zoo.__animals += 1

    def get_info(self, animal_species):
        result = ""
        if animal_species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif animal_species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif animal_species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())
for i in range(count):
    animal = input().split(" ")
    species, type_ = animal
    zoo.add_animal(species, type_)

info = input()
print(zoo.get_info(info))
