from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int ):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass


    def can_add(self, value: int):
        if  self.capacity - sum(self.ingredients.values()) - value >= 0:
            return True
        else:
            return False

    def __repr__(self):
        report = f"Factory name: {self.name} with capacity {self.capacity}.\n"
        for item in self.ingredients:
            report += f"{item}: {self.ingredients[item]}\n"
        return report


