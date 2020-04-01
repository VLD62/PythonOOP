from abc import ABC, abstractmethod

class Card(ABC):

    def __init__(self, name: str, damage_points: int, health_points: int):
        self.name = name
        self.damage_points = damage_points
        self.health_points = health_points
        if name == "":
            raise ValueError("Card's name cannot be an empty string.")
        if damage_points < 0:
            raise ValueError("Card's damage points cannot be less than zero.")
        if health_points < 0:
            raise ValueError("Card's HP cannot be less than zero.")