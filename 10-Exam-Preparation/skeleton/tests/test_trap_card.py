from project.card.trap_card import TrapCard
import unittest


class TestTrapCard(unittest.TestCase):
    def setUp(self):
        self.custom_card = TrapCard("KOZA")

    def test_init(self):
        new_card = TrapCard("KOZA")
        self.assertEqual(new_card.name, self.custom_card.name)
        self.assertEqual(self.custom_card.health_points, 5)
        self.assertEqual(self.custom_card.damage_points, 120)
        self.assertEqual(self.custom_card.__class__.__name__, "TrapCard")


    def test_constraint_card_name_cannot_be_empty(self):
        with self.assertRaises(Exception) as context:
            new_card = TrapCard("")
        self.assertEqual(str(context.exception), "Card's name cannot be an empty string.")

    def test_constraint_card_damage_points(self):
        with self.assertRaises(Exception) as context:
            self.custom_card.damage_points = -1
        self.assertEqual(str(context.exception), "Card's damage points cannot be less than zero.")

    def test_constraint_card_health_points(self):
        with self.assertRaises(Exception) as context:
            self.custom_card.health_points = -1
        self.assertEqual(str(context.exception), "Card's HP cannot be less than zero.")

    def test_add_health_points(self):
        new_card = TrapCard("KOZA")
        new_card.health_points = 62
        self.assertEqual(new_card.health_points, 62)

    def test_add_damage_points(self):
        new_card = TrapCard("KOZA")
        new_card.damage_points = 62
        self.assertEqual(new_card.damage_points, 62)


if __name__ == "__main__":
    unittest.main()
