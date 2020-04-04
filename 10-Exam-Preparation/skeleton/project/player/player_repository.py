from project.player.player import Player

class PlayerRepository:
    def __init__(self):
        self.players = []

    @property
    def count(self):
        return len(self.players)

    def add(self, player: Player):
        for existing_player in self.players:
            if existing_player.username == player.username:
                raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        for existing_player in self.players:
            if existing_player.username == player:
                self.players.remove(existing_player)

    def find(self, username: str):
        for existing_player in self.players:
            if existing_player.username == username:
                return existing_player

