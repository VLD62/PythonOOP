class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, mils):
        if self.quantity + mils <= self.size:
            self.quantity += mils

    def status(self):
        return self.size - self.quantity

if __name__ == "__main__":
    cup = Cup(100, 50)
    cup.fill(50)
    cup.fill(10)
    print(cup.status())
