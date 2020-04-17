import random
import unittest

# Import modules to test
from basic_sorting.insertionsort import insertionsort

def _create_list_of_integers(n):
    """Create a list of n integers."""
    list = []
    for _ in range(n):
        list.append(random.randint(0, 100))
    
    return list

def _create_list_of_floats(n):
    """Create a list of n floats."""
    list = []
    for _ in range(n):
        list.append(random.random() * 100)
    
    return list



class TestInsertionsort(unittest.TestCase):
    def test_insertionsort__on_integers(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        self.assertEqual(insertionsort(list), sorted(list_copy))

    def test_insertionsort__on_integers_descending(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        self.assertEqual(insertionsort(list, descending=True), sorted(list_copy, reverse=True))

    def test_insertionsort__on_empty_list(self):
        self.assertEqual(insertionsort([]), [])

    def test_insertionsort__on_empty_list_descending(self):
        self.assertEqual(insertionsort([], descending=True), [])

    def test_insertionsort__on_single_float(self):
        list = _create_list_of_floats(1)
        list_copy = list[:]
        self.assertEqual(insertionsort(list), sorted(list_copy))

    def test_insertionsort__on_single_float_descending(self):
        list = _create_list_of_floats(1)
        list_copy = list[:]
        self.assertEqual(insertionsort(list, descending=True), sorted(list_copy, reverse=True))

    def test_insertionsort__error(self):
        list = [1, 4, 5.77, 2, "a"]
        self.assertRaises(TypeError, insertionsort, list)



if __name__ == "__main__":
    unittest.main(verbosity=2)