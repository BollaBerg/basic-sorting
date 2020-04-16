def bubblesort(list, descending=False):
    """
    Takes in a list as an argument, and sorts it using a "Bubble Sort"-algorithm.

    The list can be any length and contain any number of elements, as long as they have a 
    defined "__lt__" (<)-operator.

    Selection sort has a time complexity of O(n^2), but it it performs well on lists that are
    substantially sorted, meaning they have a small number of changes required.
    For more information, check out wikipedia: https://en.wikipedia.org/wiki/Selection_sort
    """
    unsorted_numbers = len(list)

    if descending:
        while unsorted_numbers >= 1:
            last_unsorted_index = 0
            
            for i in range(1, unsorted_numbers):
                if list[i-1] < list[i]:
                    list[i], list[i-1] = list[i-1], list[i]
                    last_unsorted_index = i
            
            unsorted_numbers = last_unsorted_index

    else: # Not descending, so must be ascending (low to high)
        while unsorted_numbers >= 1:
            last_unsorted_index = 0
            
            for i in range(1, unsorted_numbers):
                if list[i] < list[i-1]:
                    list[i], list[i-1] = list[i-1], list[i]
                    last_unsorted_index = i
            
            unsorted_numbers = last_unsorted_index

    return list