import unittest
from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.custom_player = Beginner("KOZA_BEGINNER")

    def test_init(self):
        new_player = Beginner("KOZA_BEGINNER")
        self.assertEqual(new_player.username, self.custom_player.username)
        self.assertEqual(self.custom_player.health, 50)
        self.assertEqual(self.custom_player.is_dead, False)
        self.assertEqual(self.custom_player.card_repository.__class__.__name__, "CardRepository")

    def test_player_name_constraint(self):
        with self.assertRaises(Exception) as context:
            new_player = Beginner("")
        self.assertEqual(str(context.exception), "Player's username cannot be an empty string.")

    def test_player_health_constraint(self):
        with self.assertRaises(Exception) as context:
            self.custom_player.take_damage(51)
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_player_take_damage(self):
        with self.assertRaises(Exception) as context:
            self.custom_player.take_damage(-5)
        self.assertEqual(str(context.exception), "Damage points cannot be less than zero.")

    def test_player_is_dead(self):
        self.custom_player.take_damage(50)
        self.assertTrue(self.custom_player.is_dead)


if __name__ == "__main__":
    unittest.main()
