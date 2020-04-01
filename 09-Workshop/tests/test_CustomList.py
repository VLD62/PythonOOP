import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

#Coverage report is generated via coverage run --omit 'venv/*' -m unittest tests/*.py && coverage  html
#without html: coverage run --omit 'venv/*' -m unittest tests/*.py && coverage report -m

from CustomList import CustomList
import unittest

class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.custom_list = CustomList("KOZA", "KON", "BALON", 1, 1962, 15)
        self.expected_list = ["KOZA", "KON", "BALON", 1, 1962, 15]

    def test_init(self):
        self.assertEqual(self.custom_list.listche, self.expected_list)

    def test_str_repr(self):
        expected_list_str_represent = f"""['{"', '".join([str(elem) for elem in self.expected_list])}']"""
        self.assertEqual(str(self.custom_list), expected_list_str_represent)

    def test_append(self):
        self.custom_list.append(5)
        self.assertEqual(self.custom_list.listche[-1], 5)

    def test_remove(self):
        self.assertEqual(self.custom_list.listche, self.expected_list)
        self.custom_list.remove(0)
        self.assertEqual(self.custom_list.listche, self.expected_list[1:])

    def test_get(self):
        self.assertEqual(self.custom_list.get(0), self.expected_list[0])

    def test_extend(self):
        self.custom_list.extend(["LAMPA", 23, "BETONOVOZ"])
        self.assertEqual(self.custom_list.listche, ['KOZA', 'KON', 'BALON', 1, \
                         1962, 15, 'LAMPA', 23, 'BETONOVOZ'])

    def test_insert(self):
        self.custom_list.insert(2, "BOMBON")
        self.assertEqual(self.custom_list.listche[2], "BOMBON")

    def test_pop(self):
        expected_value = self.custom_list.listche[-1]
        actual_value = self.custom_list.pop()
        self.assertEqual(actual_value, expected_value)
        self.assertEqual(self.custom_list.listche, \
                         self.expected_list[:len(self.expected_list) - 1])

    def test_clear(self):
        self.custom_list.clear()
        self.assertEqual(self.custom_list.listche, [])

    def test_index(self):
        self.assertEqual(0, self.custom_list.index("KOZA"))

    def test_count(self):
        self.assertEqual(1, self.custom_list.count("KON"))

    def test_reverse(self):
        self.assertEqual(self.custom_list.reverse(), self.expected_list[::-1])

    def test_copy(self):
        copy_list = self.custom_list.copy()
        self.custom_list.clear()
        self.assertEqual(copy_list, self.expected_list)

    def test_size(self):
        self.assertEqual(self.custom_list.size(), 6)

    def test_add_first(self):
        self.custom_list.add_first(62)
        self.assertEqual(self.custom_list.listche[0], 62)

    def test_dictionize(self):
        expected_dict = {'KOZA': 'KON', 'BALON': 1, 1962: 15}
        self.assertEqual(self.custom_list.dictionize(), expected_dict)

    def test_move(self):
        expected_list = ["BALON", 1, 1962, 15, "KOZA", "KON"]
        actual_list = self.custom_list.move(2)
        self.assertEqual(actual_list, expected_list)
        self.assertEqual(self.custom_list.listche, expected_list)

    def test_sum(self):
        self.assertEqual(self.custom_list.sum(), 1990)

    def test_overbound(self):
        self.assertEqual(self.custom_list.overbound(), 4)

    def test_underbound(self):
        self.assertEqual(self.custom_list.underbound(), 3)

    #TEST Abstraction:
    # def test_underbound(self):
    #     self.assertEqual(CustomList.__base__.__name__, "ABC")


if __name__ == "__main__":
    unittest.main()
