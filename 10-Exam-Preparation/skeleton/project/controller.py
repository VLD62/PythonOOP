from battle_field import BattleField
from player.player import Player
from player.beginner import Beginner
from player.advanced import Advanced
from player.player_repository import PlayerRepository
from card.card import Card
from card.magic_card import MagicCard
from card.trap_card import TrapCard
from card.card_repository import CardRepository

class Controller:

    def __init__(self, player_repository: PlayerRepository, card_redpository: CardRepository):
        self.player_repository = player_repository
        self.card_redpository = card_redpository

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            new_player = Beginner(username)
            self.player_repository.add(new_player)
            return(f"Successfully added player of type {type} with username: {username}")
        elif type == "Advanced":
            new_player = Advanced(username)
            self.player_repository.add(new_player)
            return(f"Successfully added player of type {type} with username: {username}")
        else:
            raise ValueError("Unknown player type")

    def add_card(self, type: str, name: str):
        if type == "Magic":
            new_card = MagicCard(name)
            self.card_redpository.add(new_card)
            return(f"Successfully added card of type {type}Card with name: {name}")
        elif type == "Trap":
            new_card = TrapCard(name)
            self.card_redpository.add(new_card)
            return(f"Successfully added card of type {type}Card with name: {name}")
        else:
            raise ValueError("Unknown card type")

    def add_player_card(self, username: str, card_name: str):

        for player in self.player_repository:
            if player.username == username:
                for card in self.card_redpository:
                    if card.name == card_name:
                        player.card_repository.add(card)

    def fight(self, attack_name: str, enemy_name: str):
        attacker = None
        enemy = None
        for player in self.player_repository:
            if player.username == attack_name:
                attacker = player
            if player.username == enemy_name:
                enemy = player
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        report_msg = ""
        for player in self.player_repository:
            report_msg += f"Username: {player.username} - Health: {player.health} - Cards {player.card_repository.Count}\n"
            for card in player.card_repository:
                report_msg += f"### Card: {card.name} - Damage: {card.damage_points}\n"