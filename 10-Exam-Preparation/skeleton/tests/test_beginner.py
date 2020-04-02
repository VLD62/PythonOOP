from project.player.beginner import Beginner
import unittest

class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.custom_player = Beginner("KOZA_BEGINNER")

    def test_init(self):
        new_player = Beginner("KOZA_BEGINNER")
        self.assertEqual(new_player.username, self.custom_player.username)
        self.assertEqual(self.custom_player.health, 50)

    def test_player_health_constraint(self):
        with self.assertRaises(Exception) as context:
            self.custom_player.health = -5
        self.assertEqual(str(context.exception), "Player's health bonus cannot be less than zero.")

    def test_player_take_damage(self):
        with self.assertRaises(Exception) as context:
            self.custom_player.take_damage(-5)
        self.assertEqual(str(context.exception), "Damage points cannot be less than zero.")


if __name__ == "__main__":
    unittest.main()
