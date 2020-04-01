from abc import ABC, abstractmethod

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from project.card_repository import CardRepository

class Player(ABC):

    card_repository = CardRepository()
    is_dead = False

    def __init__(self, username: str, health: int):
        self.username = username
        self.health = health

    def take_damage(self, damage_points: int):
        if self.health - damage_points < 0:
            raise ValueError("Damage points cannot be less than zero.")
        else:
           self.health -= damage_points