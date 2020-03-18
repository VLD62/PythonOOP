from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity

class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size  = wing_size


    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return f"Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.25
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"



class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return f"Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * 0.35


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Squeak"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.10
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"



class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Woof!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.40
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"Meow"

    def feed(self, food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 0.30
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return f"ROAR!!!"

    def feed(self, food):
        if isinstance(food, Meat):
            self.food_eaten += food.quantity
            self.weight += food.quantity * 1.00
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
