from project.card.card import Card

class TrapCard(Card):
    def __init__(self, name: str):
        super().__init__(name)
        self.damage_points = 120
        self.health_points = 5