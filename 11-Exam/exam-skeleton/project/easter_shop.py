from project.factory.factory import Factory
from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop():

    def __init__(self, name: str, chocolate_factory: ChocolateFactory, egg_factory: EggFactory, paint_factory: PaintFactory):
        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage =  {}

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(ingredient_type=type, quantity=quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(ingredient_type=type, quantity=quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(ingredient_type=type, quantity=quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        self.storage[recipe] = 1

    def paint_egg(self, color: str, egg_type: str):
        if egg_type in self.egg_factory.ingredients:
            if color in self.paint_factory.ingredients:
                egg_color_type = f"{color} {egg_type}"
                if egg_color_type in self.storage:
                    self.storage[egg_color_type] += 1
                else:
                    self.storage[egg_color_type] = 1
            else:
                raise ValueError("Invalid commands")
        else:
            raise ValueError("Invalid commands")

    def __repr__(self):
        report = f"Shop name: {self.name}\nShop Storage:\n"
        for item_name, item_qty in self.storage.items():
            report += f"{item_name}: {item_qty}\n"
        return report
