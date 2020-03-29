import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)


from project.list import IntegerList
import unittest

class TestIntegerList(unittest.TestCase):
    def test_init_no_arguments_create_empty_data(self):
        data = []
        integer_list = IntegerList(*data)
        expected = []
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_init_with_int_args_add_elements_data(self):
        data = [1, 2, 3]
        integer_list = IntegerList(*data)
        expected = [1, 2, 3]
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_init_with_non_integer_args_not_add_elements_data(self):
        data = ["one", 3]
        integer_list = IntegerList(*data)
        expected = [3]
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_get_data(self):
        data = [1, 3]
        integer_list = IntegerList(*data)
        actual = integer_list.get_data()
        self.assertEqual(actual, data)

    def test_remove_index(self):
        data = [1, 3]
        integer_list = IntegerList(*data)
        actual = integer_list.remove_index(0)
        expected = 1
        self.assertEqual(actual, expected)
        expected = [3]
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_remove_index_out_of_range(self):
        data = [1, 3]
        integer_list = IntegerList(*data)
        with self.assertRaises(IndexError) as context:
            integer_list.remove_index(2)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_add_element(self):
        data = [1, 3]
        integer_list = IntegerList(*data)
        integer_list.add(6)
        expected = [1, 3, 6]
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_add_element_non_int(self):
        data = [1, 3]
        integer_list = IntegerList(*data)
        with self.assertRaises(ValueError) as context:
            integer_list.add("six")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_element(self):
        data = [1, 3]
        integer_list = IntegerList(*data)
        actual = integer_list.get(0)
        self.assertEqual(actual, data[0])

    def test_get_element_out_of_range(self):
        data = [1, 3]
        integer_list = IntegerList(*data)
        with self.assertRaises(IndexError) as context:
            integer_list.get(3)
        self.assertEqual(str(context.exception), "Index is out of range")


if __name__ == "__main__":
    unittest.main()