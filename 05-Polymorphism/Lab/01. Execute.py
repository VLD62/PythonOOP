def execute(func, *args):
    return func(*args)


def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")

def say_bye(name):
    print(f"Bye, {name}")

def test_func_ok(name, age):
    print(f"I am {name} and I am {age} years old")

execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")
execute(test_func_ok, "Tanya", 22)


import unittest

class ExecuteTest(unittest.TestCase):
    def test(self):
        def test_func(name, age):
            return f"I am {name} and I am {age} years old"
        res = execute(test_func, "Tanya", 22)
        self.assertEqual(res, "I am Tanya and I am 22 years old")

if __name__ == '__main__':
    unittest.main()