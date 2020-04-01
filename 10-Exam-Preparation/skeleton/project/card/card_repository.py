from card import Card

class CardRepository:
    def __init__(self, Count: int, Cards: list):
        self.Count = 0
        self.Cards = []

    def add(self, card: Card):
        for existing_card in self.Cards:
            if card.name == existing_card.name:
                raise ValueError(f"Card {card.name} already exists!")
            else:
                self.Cards.append(card)
                self.Count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        else:
            for existing_card in self.Cards:
                if existing_card.name == card:
                    self.Cards.remove(existing_card)
                    self.Count -= 1

    def find(self, name: str):
        for existing_card in self.Cards:
            if existing_card.name == name:
                return existing_card