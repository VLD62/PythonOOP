class Animal:
    @classmethod
    def eat(cls):
        return f"eating..."


class Dog(Animal):
    @classmethod
    def bark(cls):
        return f"barking..."


class Cat(Animal):
    @classmethod
    def meow(cls):
        return f"meowing..."
