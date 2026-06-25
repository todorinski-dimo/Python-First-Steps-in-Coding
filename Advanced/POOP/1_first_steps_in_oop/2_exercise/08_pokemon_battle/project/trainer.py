from project.pokemon import Pokemon

class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, ap_pokemon: Pokemon):
        if ap_pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(ap_pokemon)
        return f"Caught {ap_pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pk in self.pokemons:
            if pokemon_name == pk.name:
                self.pokemons.remove(pk)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result_str = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"
        for item in self.pokemons:
            result_str += f"\n- {item.pokemon_details()}"
        return result_str

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
trainer.add_pokemon(Pokemon("Charizard1", 110))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
