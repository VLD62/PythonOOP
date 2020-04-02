from project.card.trap_card import TrapCard
import unittest

class TestTrapCard(unittest.TestCase):
    def setUp(self):
        self.custom_card = TrapCard("KOZA")

    def test_init(self):
        new_card = TrapCard("KOZA")


    def test_check_card_name_cannot_be_empty(self):
        with self.assertRaises(Exception) as context:
            new_card = TrapCard("")
        self.assertEqual(str(context.exception), "Card's name cannot be an empty string.")

if __name__ == "__main__":
    unittest.main()
