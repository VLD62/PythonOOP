from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.cards = []

    def add(self, card: Card):
        for existing_card in self.cards:
            if card.name == existing_card.name:
                raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)

    def remove(self, card_name: str):
        if card_name == "":
            raise ValueError("Card cannot be an empty string!")
        for existing_card in self.cards:
            if existing_card.name == card_name:
                self.cards.remove(existing_card)

    def find(self, name: str):
        for existing_card in self.cards:
            if existing_card.name == name:
                return existing_card

    @property
    def count(self):
        return len(self.cards)
