import unittest
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.card.card_repository import CardRepository


class TestCardRepository(unittest.TestCase):

    def setUp(self):
        self.magic_card = MagicCard("KOZA_MAGIC")
        self.trap_card = TrapCard("KOZA_TRAP")
        self.new_repository = CardRepository()

    def test_init(self):
        self.assertEqual(self.new_repository.__class__.__name__, "CardRepository")
        self.assertEqual(self.new_repository.cards, [])
        self.assertEqual(self.new_repository.count, 0)

    def test_add_card_increase_count(self):
        self.assertEqual(self.new_repository.count, 0)
        self.new_repository.add(self.trap_card)
        self.assertEqual(self.new_repository.count, 1)

    def test_add_card_duplicate_name(self):
        self.new_repository.add(self.trap_card)
        with self.assertRaises(Exception) as context:
            self.new_repository.add(self.trap_card)
        self.assertEqual(str(context.exception), f"Card {self.trap_card.name} already exists!")

    def test_remove_card_decrease_count(self):
        self.new_repository.add(self.trap_card)
        self.assertEqual(self.new_repository.count, 1)
        self.new_repository.remove(self.trap_card.name)
        self.assertEqual(self.new_repository.count, 0)
        self.assertEqual(self.new_repository.cards, [])

    def test_remove_card_empty_name(self):
        with self.assertRaises(Exception) as context:
            self.new_repository.remove("")
        self.assertEqual(str(context.exception), "Card cannot be an empty string!")

    def test_find_card(self):
        self.new_repository.add(self.magic_card)
        self.assertEqual(self.new_repository.count, 1)
        expected_card = self.new_repository.find(self.magic_card.name)
        self.assertEqual(expected_card.__class__.__name__, "MagicCard")
        self.assertEqual(expected_card.name, self.magic_card.name)


if __name__ == "__main__":
    unittest.main()