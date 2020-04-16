import random
from selectionsort import selectionsort

def _create_list(n):
    list = []
    for _ in range(n):
        list.append(random.randint(0, 100))
    
    return list


def test_selectionsort():
    list = _create_list(25)
    list_copy = list[:]

    print(F"Unsorted list:\t\t {list}")
    print(F"Own sorted list:\t {selectionsort(list)}")
    print(F"Python-sorted list:\t {sorted(list_copy)}")

if __name__ == '__main__':
    test_selectionsort()