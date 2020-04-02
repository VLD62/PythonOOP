from project.card.card import Card

class CardRepository:

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        for existing_card in self.cards:
            if card.name == existing_card.name:
                raise ValueError(f"Card {card.name} already exists!")
            else:
                self.cards.append(card)
                self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        else:
            for existing_card in self.cards:
                if existing_card.name == card:
                    self.cards.remove(existing_card)
                    self.count -= 1

    def find(self, name: str):
        for existing_card in self.cards:
            if existing_card.name == name:
                return existing_card