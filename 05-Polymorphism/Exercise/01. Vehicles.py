from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self,distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.__ac_fuel_consumption = 0.9

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.__ac_fuel_consumption)
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
        self.__ac_fuel_consumption = 1.6

    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.__ac_fuel_consumption)
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel


    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


# second zero test
import unittest

class VehiclesTests(unittest.TestCase):
    def test_second_zero(self):
        truck = Truck(100, 15)
        truck.drive(5)
        self.assertEqual(truck.fuel_quantity, 17.0)
        truck.refuel(50)
        self.assertEqual(truck.fuel_quantity, 64.5)

if __name__ == '__main__':
    unittest.main()