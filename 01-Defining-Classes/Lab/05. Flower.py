class Flower():
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, qty):
        if qty >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"


if __name__ == "__main__":
    flower = Flower("Lilly", 100)
    flower.water(50)
    print(flower.status())
    flower.water(100)
    print(flower.status())
