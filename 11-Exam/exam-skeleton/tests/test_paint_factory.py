import unittest
from project.factory.paint_factory import PaintFactory



class TestPaintFactory(unittest.TestCase):

    def setUp(self):
        self.paint_factory = PaintFactory("KOZA_FACTORY", 10)

    def test_init(self):
        self.assertEqual(self.paint_factory.name, "KOZA_FACTORY")
        self.assertEqual(self.paint_factory.capacity, 10)
        self.assertEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.__class__.__name__, "PaintFactory")

    def test_can_add_ok(self):
        self.assertTrue(self.paint_factory.can_add(10))

    def test_can_add_not(self):
        self.assertFalse(self.paint_factory.can_add(11))

    def test_add_ingerdient_ok(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients["white"], 2)

    def test_add_ingerdient_no_space(self):
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient("white", 11)
        self.assertEqual(str(context.exception), "Not enough space in factory")


    def test_add_ingredient_type_not_allowed(self):
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient("kon", 11)
        self.assertEqual(str(context.exception), f"Ingredient of type kon not allowed in {self.paint_factory.__class__.__name__}")

    def test_remove_ingredient_ok(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients["white"], 2)
        self.paint_factory.remove_ingredient("white", 1)
        self.assertEqual(self.paint_factory.ingredients["white"], 1)
        self.paint_factory.remove_ingredient("white", 1)
        self.assertEqual(self.paint_factory.ingredients["white"], 0)

    def test_remove_ingredient_no_such_product(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients["white"], 2)
        with self.assertRaises(KeyError) as context:
                    self.paint_factory.remove_ingredient("black", 1)
        self.assertEqual(str(context.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_qty_less_zero(self):
        self.paint_factory.add_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients["white"], 2)
        with self.assertRaises(ValueError) as context:
                    self.paint_factory.remove_ingredient("white", 5)
        self.assertEqual(str(context.exception), "Ingredient quantity cannot be less than zero")

    def test_products_property(self):
        self.paint_factory.add_ingredient("white", 2)
        self.paint_factory.add_ingredient("blue", 3)
        self.assertEqual(self.paint_factory.products, {'white': 2, 'blue': 3})

    def test_report(self):
        self.paint_factory.add_ingredient("white", 2)
        self.paint_factory.add_ingredient("blue", 3)
        expected_report = "Factory name: KOZA_FACTORY with capacity 10.\nwhite: 2\nblue: 3\n"
        actual_report = self.paint_factory
        self.assertEqual(str(actual_report), expected_report)

if __name__ == "__main__":
    unittest.main()



