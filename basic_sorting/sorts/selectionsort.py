def selectionsort(list, descending=False):
    """
    Takes in a list as an argument, and sorts it using a "Selection Sort"-algorithm.

    The list can be any length and contain any number of elements, as long as they have a 
    defined "__lt__" (<)-operator.

    Selection sort has a time complexity of O(n^2), but a maximum of n-1 swaps makes it viable if
    swapping is expensive. For more information, check out wikipedia: https://en.wikipedia.org/wiki/Selection_sort
    """
    length = len(list)

    if descending:
        for i in range(length):
            max_element_index = i

            for j in range (i+1, length):
                if list[max_element_index] < list[j]:
                    max_element_index = j
            
            if max_element_index != i:
                list[i], list[max_element_index] = list[max_element_index], list[i]

    else:   # Not descending, so must be ascending (low to high)
        for i in range(length):
            min_element_index = i

            for j in range (i+1, length):
                if list[j] < list[min_element_index]:
                    min_element_index = j
            
            if min_element_index != i:
                list[i], list[min_element_index] = list[min_element_index], list[i]

    return list