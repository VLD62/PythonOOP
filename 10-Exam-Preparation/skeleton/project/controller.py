from project.battle_field import BattleField
from project.player.player import Player
from project.player.beginner import Beginner
from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository
from project.card.card import Card
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.card.card_repository import CardRepository

class Controller:

    def __init__(self, player_repository: PlayerRepository, card_repository: CardRepository):
        self.player_repository = player_repository
        self.card_repository = card_repository

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            new_player = Beginner(username)
            self.player_repository.add(new_player)

        if type == "Advanced":
            new_player = Advanced(username)
            self.player_repository.add(new_player)

        return f"Successfully added player of type {type} with username: {username}"


    def add_card(self, type: str, name: str):
        if type == "Magic":
            new_card = MagicCard(name)
            self.card_repository.add(new_card)

        if type == "Trap":
            new_card = TrapCard(name)
            self.card_repository.add(new_card)

        return f"Successfully added card of type {type}Card with name: {name}"


    def add_player_card(self, username: str, card_name: str):
        for player in self.player_repository:
            if player.username == username:
                for card in self.card_repository:
                    if card.name == card_name:
                        player.card_repository.add(card)
                        return f"Successfully added card: {card_name} to user: {username}"

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
        return report_msg