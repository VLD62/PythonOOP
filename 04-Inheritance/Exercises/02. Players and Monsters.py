class Hero:
    def __init__(self, username: str, level: int):
        self.username  = username
        self.level = level

    def __repr__(self):
        return f"{self.name} of type {Hero.__class__.__name__} has level {self.level}"

class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return Hero.__repr__(self)

class MuseElf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return Elf.__repr__(self)


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return Hero.__repr__(self)

class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return Wizard.__repr__(self)


class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return DarkWizard.__repr__(self)

class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return Hero.__repr__(self)

class DarkKnight(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return Knight.__repr__(self)

class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return DarkKnight.__repr__(self)