class Person:
    @classmethod
    def sleep(cls):
        return f"sleeping..."


class Employee:
    @classmethod
    def get_fired(cls):
        return f"fired..."


class Teacher(Person, Employee):
    @classmethod
    def teach(cls):
        return f"teaching..."