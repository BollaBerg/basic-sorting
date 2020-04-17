import random
import pytest

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



class TestInsertionsortAscending:
    def test_insertionsort__on_integers(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        assert insertionsort(list) == sorted(list_copy)
    
    def test_insertionsort__on_empty_list(self):
        assert insertionsort([]) == []

    def test_insertionsort__on_single_float(self):
        list = _create_list_of_floats(1)
        list_copy = list[:]
        assert insertionsort(list) == sorted(list_copy)

    def test_insertionsort__error(self):
        list = [1, 4, 5.77, 2, "a"]
        with pytest.raises(TypeError):
            insertionsort(list)



class TestInsertionsortDescending:
    def test_insertionsort__on_integers_descending(self):
        list = _create_list_of_integers(25)
        list_copy = list[:]
        assert insertionsort(list, descending=True) == sorted(list_copy, reverse=True)

    def test_insertionsort__on_empty_list_descending(self):
        assert insertionsort([], descending=True) == []

    def test_insertionsort__on_single_float_descending(self):
        list = _create_list_of_floats(1)
        list_copy = list[:]
        assert insertionsort(list, descending=True) == sorted(list_copy, reverse=True)

    def test_insertionsort__error_descending(self):
        list = [1, 4, 5.77, 2, "a"]
        with pytest.raises(TypeError):
            insertionsort(list, descending=True)



if __name__ == "__main__":
    pytest.main(["--verbose", __file__])