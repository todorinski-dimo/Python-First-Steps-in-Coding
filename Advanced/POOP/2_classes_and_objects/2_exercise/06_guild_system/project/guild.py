from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"


    def kick_player(self, name: str):
        found_player = next((p for p in self.players if p.name == name), None)
        if found_player:
            found_player.guild = "Unaffiliated"
            self.players.remove(found_player)
            return f"Player {name} has been removed from the guild."
        return f"Player {name} is not in the guild."

    def guild_info(self):
        return (f"Guild: {self.name}\n" +
                "\n".join(f"{p.player_info()}" for p in self.players))
