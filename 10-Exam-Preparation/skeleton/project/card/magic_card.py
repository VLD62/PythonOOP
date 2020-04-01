from card import Card

class MagicCard(Card):
    def __init__(self, name: str):
        super().__init__(name)
        self.damage_points = 5
        self.health_points = 80