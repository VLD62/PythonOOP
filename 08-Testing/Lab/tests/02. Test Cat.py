import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


from skeleton.Cat import Cat
import unittest

class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat(name="Boyko Borissov")

    def test_init(self):
        self.assertEqual([self.cat.name, self.cat.fed, self.cat.sleepy, self.cat.size], \
            ["Boyko Borissov", False, False, 0])

    def test_eat(self):
        ref_size = self.cat.size
        self.cat.eat()
        self.assertEqual([self.cat.fed, self.cat.sleepy, self.cat.size], \
            [ True, True, ref_size + 1])
        with self.assertRaises(Exception) as context:
            self.cat.eat()
        self.assertEqual(str(context.exception), "Already fed.")

    def test_sleep(self):
        with self.assertRaises(Exception) as context:
            self.cat.sleep()
        self.assertEqual(str(context.exception), "Cannot sleep while hungry")
        self.cat.eat()
        self.assertEqual(self.cat.sleepy, True)
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)

if __name__ == "__main__":
    unittest.main()