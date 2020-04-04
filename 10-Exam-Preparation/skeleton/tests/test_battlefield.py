import unittest
from project.battle_field import BattleField
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class TestBattleField(unittest.TestCase):

    def setUp(self):
        self.battle_field = BattleField()
        self.beginner_player = Beginner("KOZA_BEGINNER")
        self.advanced_player = Advanced("KOZA_ADVANCED")
        self.new_trap_card = TrapCard("KOZA_TRAP")
        self.new_magic_card = MagicCard("KOZA_MAGIC")
        self.beginner_player.card_repository.add(self.new_trap_card)
        self.advanced_player.card_repository.add(self.new_magic_card)

    def test_get_bonus_health_damage(self):
        self.assertEqual(self.beginner_player.card_repository.cards[0].damage_points, 120)
        self.assertEqual(self.advanced_player.card_repository.cards[0].damage_points, 5)
        beginner_expected = self.battle_field.get_bonus_health_damage(self.beginner_player)
        advanced_expected = self.battle_field.get_bonus_health_damage(self.advanced_player)
        self.assertEqual(beginner_expected, 45)
        self.assertEqual(advanced_expected, 80)
        self.assertEqual(self.beginner_player.card_repository.cards[0].damage_points, 150)
        self.assertEqual(self.advanced_player.card_repository.cards[0].damage_points, 5)

    def test_fight_two_begginer_players(self):
        new_beginner_player = Beginner("KOZA_BEGINNER_NEW")
        new_second_trap_card = TrapCard("KOZA_TRAP_SECOND")
        new_beginner_player.card_repository.add(new_second_trap_card)
        with self.assertRaises(Exception) as context:
            self.battle_field.fight(self.beginner_player, new_beginner_player)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")


    def test_fight_beginner_as_attacker(self):
        self.battle_field.fight(self.beginner_player, self.advanced_player)
        self.assertFalse(self.beginner_player.is_dead)
        self.assertFalse(self.advanced_player.is_dead)
        self.assertEqual(self.beginner_player.health, 90)
        self.assertEqual(self.advanced_player.health, 180)

    def test_fight_advanced_as_attacker(self):
        self.battle_field.fight(self.advanced_player, self.beginner_player)
        self.assertFalse(self.beginner_player.is_dead)
        self.assertFalse(self.advanced_player.is_dead)
        self.assertEqual(self.beginner_player.health, 90)
        self.assertEqual(self.advanced_player.health, 180)

    def test_fight_beginner_as_attacker_with_additional_cards(self):
        new_second_trap_card = TrapCard("KOZA_TRAP_SECOND")
        new_third_trap_card = TrapCard("KOZA_TRAP_THIRD")
        self.beginner_player.card_repository.add(new_second_trap_card)
        self.beginner_player.card_repository.add(new_third_trap_card)
        with self.assertRaises(Exception) as context:
            self.battle_field.fight(self.beginner_player, self.advanced_player)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_fight_advanced_as_attacker_with_additional_cards(self):
        new_second_trap_card = TrapCard("KOZA_TRAP_SECOND")
        new_third_trap_card = TrapCard("KOZA_TRAP_THIRD")
        self.advanced_player.card_repository.add(new_second_trap_card)
        self.advanced_player.card_repository.add(new_third_trap_card)
        with self.assertRaises(Exception) as context:
            self.battle_field.fight(self.advanced_player, self.beginner_player)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_fight_beginner_as_attacker_with_additional_cards_advanced(self):
        new_second_trap_card = TrapCard("KOZA_TRAP_SECOND")
        new_third_trap_card = TrapCard("KOZA_TRAP_THIRD")
        self.advanced_player.card_repository.add(new_second_trap_card)
        self.advanced_player.card_repository.add(new_third_trap_card)
        with self.assertRaises(Exception) as context:
            self.battle_field.fight(self.beginner_player, self.advanced_player)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_fight_advanced_as_attacker_with_additional_cards_beginner(self):
        new_second_trap_card = TrapCard("KOZA_TRAP_SECOND")
        new_third_trap_card = TrapCard("KOZA_TRAP_THIRD")
        self.beginner_player.card_repository.add(new_second_trap_card)
        self.beginner_player.card_repository.add(new_third_trap_card)
        with self.assertRaises(Exception) as context:
            self.battle_field.fight(self.advanced_player, self.beginner_player)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_dead_player(self):
        self.beginner_player.health = 0
        with self.assertRaises(Exception) as context:
            self.battle_field.fight(self.beginner_player, self.advanced_player)
        self.assertEqual(str(context.exception), "Player is dead!")
        self.beginner_player.health = 50
        self.advanced_player.health = 0
        with self.assertRaises(Exception) as context:
            self.battle_field.fight(self.beginner_player, self.advanced_player)
        self.assertEqual(str(context.exception), "Player is dead!")


if __name__ == "__main__":
    unittest.main()
