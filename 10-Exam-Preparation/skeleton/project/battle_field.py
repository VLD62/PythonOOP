# import sys, os
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir)

from player.player_repository import PlayerRepository
from player.player import Player
from player.beginner import Beginner


class BattleField:

    def calculate_total_damage(self, player: Player):
        total_damage  =  0
        for card in player.card_repository:
            total_damage += card.damage_points
        return total_damage


    def get_bonus_health(self, player: Player):
        for card in player.card_repository:
            player.health += card.health_points

    def check_beginner(self, player: Player):
        if isinstance(player, Beginner):
            player.health += 40
            for card in player.card_repository:
                card.damage_points += 30

    def fight(self, attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        self.check_beginner(attacker)
        self.check_beginner(enemy)
        self.get_bonus_health(attacker)
        self.get_bonus_health(enemy)
        attacker_total_damage = self.calculate_total_damage(attacker)
        enemy_total_damage = self.calculate_total_damage(enemy)
        if attacker_total_damage >= enemy.health:
            enemy.is_dead = True
            return
        else:
            enemy.health -= attacker_total_damage
        if enemy_total_damage >= attacker.health:
            attacker.is_dead = True
            return
        else:
            attacker.health -= enemy_total_damage