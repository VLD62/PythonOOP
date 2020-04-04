import unittest
from project.controller import Controller
from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class TestController(unittest.TestCase):

    def setUp(self):
        self.new_controller = Controller()
        self.beginner_player = Beginner("KOZA_BEGINNER")
        self.advanced_player = Advanced("KOZA_ADVANCED")
        self.magic_card = MagicCard("KOZA_MAGIC")
        self.trap_card = TrapCard("KOZA_TRAP")

    def test_init(self):
        self.assertEqual(self.new_controller.player_repository.__class__.__name__, "PlayerRepository")
        self.assertEqual(self.new_controller.card_repository.__class__.__name__, "CardRepository")
        self.assertEqual(self.new_controller.player_repository.count, 0)
        self.assertEqual(self.new_controller.card_repository.count, 0)
        self.assertEqual(self.new_controller.player_repository.players, [])
        self.assertEqual(self.new_controller.card_repository.cards, [])

    def test_add_player_beginner(self):
        actual_result = self.new_controller.add_player(type="Beginner", username="PESHO")
        expected_result = "Successfully added player of type Beginner with username: PESHO"
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.new_controller.player_repository.find("PESHO").username, "PESHO")
        self.assertEqual(type(self.new_controller.player_repository.find("PESHO")).__name__, "Beginner")

    def test_add_player_advanced(self):
        actual_result = self.new_controller.add_player(type="Advanced", username="GOSHO")
        expected_result = "Successfully added player of type Advanced with username: GOSHO"
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.new_controller.player_repository.find("GOSHO").username, "GOSHO")
        self.assertEqual(type(self.new_controller.player_repository.find("GOSHO")).__name__, "Advanced")

    def test_add_card_magic(self):
        actual_result = self.new_controller.add_card(type="Magic", name="KOZA_MAGIC")
        expected_result = "Successfully added card of type MagicCard with name: KOZA_MAGIC"
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.new_controller.card_repository.find("KOZA_MAGIC").name, "KOZA_MAGIC")
        self.assertEqual(type(self.new_controller.card_repository.find("KOZA_MAGIC")).__name__, "MagicCard")

    def test_add_card_trap(self):
        actual_result = self.new_controller.add_card(type="Trap", name="KOZA_TRAP")
        expected_result = "Successfully added card of type TrapCard with name: KOZA_TRAP"
        self.assertEqual(actual_result, expected_result)
        self.assertEqual(self.new_controller.card_repository.find("KOZA_TRAP").name, "KOZA_TRAP")
        self.assertEqual(type(self.new_controller.card_repository.find("KOZA_TRAP")).__name__, "TrapCard")

    def test_add_player_card(self):
        self.new_controller.add_card(type="Trap", name="KOZA_TRAP")
        self.new_controller.add_player(type="Advanced", username="GOSHO")
        actual_result = self.new_controller.add_player_card(username="GOSHO", card_name="KOZA_TRAP")
        expected_result = "Successfully added card: KOZA_TRAP to user: GOSHO"
        actual_card = self.new_controller.player_repository.find("GOSHO").card_repository.find("KOZA_TRAP")
        self.assertEqual(actual_card.name, "KOZA_TRAP")
        self.assertEqual(actual_result, expected_result)

    def test_fight(self):
        self.new_controller.add_player("Beginner", "PESHO")
        self.new_controller.add_player("Advanced", "GOSHO")
        self.new_controller.add_card("Trap", "KOZA_TRAP")
        self.new_controller.add_player_card("PESHO", "KOZA_TRAP")
        actual_result = self.new_controller.fight("PESHO", "GOSHO")
        expected_result = "Attack user health 95 - Enemy user health 100"
        self.assertEqual(actual_result, expected_result)

    def test_report(self):
        self.new_controller.add_card(type="Magic", name="KOZA_MAGIC")
        self.new_controller.add_player(type="Beginner", username="PESHO")
        self.new_controller.add_player_card(username="PESHO", card_name="KOZA_MAGIC")
        self.new_controller.add_card(type="Trap", name="KOZA_TRAP")
        self.new_controller.add_player(type="Advanced", username="GOSHO")
        self.new_controller.add_player_card(username="GOSHO", card_name="KOZA_TRAP")
        actual_result = self.new_controller.report()
        expected_result = f"Username: PESHO - Health: 50 - Cards 1\n### Card: KOZA_MAGIC - Damage: 5\nUsername: GOSHO - Health: 250 - Cards 1\n### Card: KOZA_TRAP - Damage: 120\n"
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()