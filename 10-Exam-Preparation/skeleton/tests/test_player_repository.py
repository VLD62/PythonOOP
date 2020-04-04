from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository
import unittest


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.new_player_repository = PlayerRepository()
        self.beginner_player = Beginner("KOZA_BEGINNER")
        self.advanced_player = Advanced("KOZA_ADVANCED")

    def test_init(self):
        self.assertEqual(self.new_player_repository.__class__.__name__, "PlayerRepository")
        self.assertEqual(self.new_player_repository.players, [])
        self.assertEqual(self.new_player_repository.count, 0)

    def test_add_player(self):
        self.assertEqual(self.new_player_repository.count, 0)
        self.new_player_repository.add(self.beginner_player)
        self.new_player_repository.add(self.advanced_player)
        self.assertEqual(self.new_player_repository.count, 2)
        self.assertEqual(len(self.new_player_repository.players), 2)

    def test_add_player_duplicate_name(self):
        self.new_player_repository.add(self.beginner_player)
        self.assertEqual(self.new_player_repository.count, 1)
        with self.assertRaises(Exception) as context:
            self.new_player_repository.add(self.beginner_player)
        self.assertEqual(str(context.exception), f"Player {self.beginner_player.username} already exists!")
        self.assertEqual(len(self.new_player_repository.players), 1)

    def test_remove_player(self):
        self.new_player_repository.add(self.beginner_player)
        self.assertEqual(self.new_player_repository.count, 1)
        self.new_player_repository.remove(self.beginner_player.username)
        self.assertEqual(self.new_player_repository.count, 0)
        self.assertEqual(self.new_player_repository.players, [])

    def test_remove_empty_name(self):
        with self.assertRaises(Exception) as context:
            self.new_player_repository.remove("")
        self.assertEqual(str(context.exception), "Player cannot be an empty string!")

    def test_find_username(self):
        self.new_player_repository.add(self.beginner_player)
        self.assertEqual(self.new_player_repository.count, 1)
        expected_player = self.new_player_repository.find("KOZA_BEGINNER")
        self.assertEqual(expected_player.__class__.__name__, "Beginner")
        self.assertEqual(expected_player, self.beginner_player)

if __name__ == "__main__":
    unittest.main()
