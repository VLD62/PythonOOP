import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


from skeleton.Workers import Worker
import unittest

class TestWorkers(unittest.TestCase):
    def setUp(self):
        self.worker = Worker(name="Bai Ivan", salary=5000, energy=1)

    def test_init(self):
        self.assertEqual([self.worker.name, self.worker.salary, self.worker.energy], \
            ["Bai Ivan", 5000, 1])

    def test_work(self):
        self.assertEqual(self.worker.money, 0)
        self.worker.work()
        self.assertEqual(self.worker.energy, 0)
        self.assertEqual(self.worker.money, 5000)
        with self.assertRaises(Exception) as context:
            self.worker.work()
        self.assertEqual(str(context.exception), "Not enough energy.")

    def test_rest(self):
        ref_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy, ref_energy + 1)

    def test_get_info(self):
        self.worker.work()
        self.assertEqual(self.worker.get_info(), "Bai Ivan has saved 5000 money.")


if __name__ == "__main__":
    unittest.main()