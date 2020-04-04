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

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        result = ""
        if type == "Beginner":
            new_player = Beginner(username)
            self.player_repository.add(new_player)
            result = f"Successfully added player of type {type} with username: {username}"
        if type == "Advanced":
            new_player = Advanced(username)
            self.player_repository.add(new_player)
            result = f"Successfully added player of type {type} with username: {username}"
        return result


    def add_card(self, type: str, name: str):
        result = ""
        if type == "Magic":
            new_card = MagicCard(name)
            self.card_repository.add(new_card)
            result = f"Successfully added card of type {type}Card with name: {name}"
        if type == "Trap":
            new_card = TrapCard(name)
            self.card_repository.add(new_card)
            result = f"Successfully added card of type {type}Card with name: {name}"
        return result



    def add_player_card(self, username: str, card_name: str):
        for player in self.player_repository.players:
            if player.username == username:
                for card in self.card_repository.cards:
                    if card.name == card_name:
                        player.card_repository.add(card)
                        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name: str, enemy_name: str):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker=attacker, enemy=enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        report_msg = ""
        for player in self.player_repository.players:
            report_msg += f"Username: {player.username} - Health: {player.health} - Cards {player.card_repository.count}\n"
            for card in player.card_repository.cards:
                report_msg += f"### Card: {card.name} - Damage: {card.damage_points}\n"
        return report_msg