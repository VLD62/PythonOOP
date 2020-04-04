from project.player.player import Player


class BattleField:
    @staticmethod
    def get_bonus_health_damage(player: Player):
        bonus_health = sum([card.health_points for card in player.card_repository.cards])
        if player.__class__.__name__ == "Beginner":
            bonus_health += 40
            for card in player.card_repository.cards:
                    card.damage_points += 30
        return bonus_health

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        #Calculate bonus health and damage:
        attacker.health += BattleField.get_bonus_health_damage(attacker)
        enemy.health += BattleField.get_bonus_health_damage(enemy)

        #Fight:
        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)




