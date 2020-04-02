from abc import ABC, abstractmethod
from project.card.card_repository import CardRepository

class Player(ABC):

    @abstractmethod
    def __init__(self, username: str):
        self.__username = username
        self.health = 0
        self.card_repository = CardRepository()

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Player's username cannot be an empty string.")
        self.__username = value

    @property
    def is_dead(self):
        if self.health <= 0:
            return True
        return False

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Player's health bonus cannot be less than zero.")
        self.__health = value

    def take_damage(self, damage_points: int):
        if damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        self.health -= damage_points