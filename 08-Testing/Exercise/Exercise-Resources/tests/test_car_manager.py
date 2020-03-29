import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


from project.car_manager import Car
import unittest

class TestCarManager(unittest.TestCase):
    def setUp(self):
        self.car = Car(make="BMW", model="330d", fuel_consumption=9, fuel_capacity=50)

    def test_init(self):
        self.assertEqual([self.car.make, self.car.model, self.car.fuel_consumption, \
            self.car.fuel_capacity], ["BMW", "330d", 9, 50])

    def test_make_constraint(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")


    def test_model_constraint(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")


    def test_fuel_consumption_constraint(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_constraint(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_constraint(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_refuel(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-1)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")
        ref_fuel = 10
        self.car.refuel(ref_fuel)
        actual_fuel = self.car.fuel_amount
        self.assertEqual(actual_fuel, ref_fuel)
        fuel = 10 + self.car.fuel_capacity
        self.car.refuel(fuel)
        actual_fuel = self.car.fuel_amount
        self.assertEqual(actual_fuel, self.car.fuel_capacity)

    def test_drive(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(100)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")
        total_fuel = 50
        distance = 100
        self.car.refuel(total_fuel)
        self.car.drive(distance)
        needed_fuel = (distance / 100) * self.car.fuel_consumption
        self.assertEqual(self.car.fuel_amount, (total_fuel - needed_fuel))


if __name__ == "__main__":
    unittest.main()