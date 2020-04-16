import random
import string
import unittest

# Import modules to test
from basic_sorting.sorts.selectionsort import selectionsort, selectionsort_reversed

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

def _create_list_of_letters(n):
    """Create a list of n letters."""
    list = []
    for _ in range(n):
        random_letter = random.choice(string.ascii_letters)
        list.append(random_letter)
    
    return list



class TestSelectionsort(unittest.TestCase):
    def test_selectionsort_on_integers(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        self.assertEqual(selectionsort(list), sorted(list_copy))

    def test_selectionsort_on_integers_descending(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        self.assertEqual(selectionsort(list, descending=True), sorted(list_copy, reverse=True))

    def test_selectionsort_on_floats(self):
        list = _create_list_of_floats(25)
        list_copy = list[:]
        self.assertEqual(selectionsort(list), sorted(list_copy))

    def test_selectionsort_on_floats_descending(self):
        list = _create_list_of_floats(25)
        list_copy = list[:]
        self.assertEqual(selectionsort(list, descending=True), sorted(list_copy, reverse=True))

    def test_selectionsort_on_letters(self):
        list = _create_list_of_letters(25)
        list_copy = list[:]
        self.assertEqual(selectionsort(list), sorted(list_copy))

    def test_selectionsort_on_letters_descending(self):
        list = _create_list_of_letters(25)
        list_copy = list[:]
        self.assertEqual(selectionsort(list, descending=True), sorted(list_copy, reverse=True))

    def test_selectionsort_error(self):
        list = [1, 4, 5.77, 2, "a"]
        self.assertRaises(TypeError, selectionsort, list)



if __name__ == "__main__":
    unittest.main(verbosity=2)