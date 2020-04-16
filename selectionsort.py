def selectionsort(list):
    """
    Takes in a list as an argument, and sorts it using a "Selection Sort"-algorithm.

    The list can be any length and contain any number of elements, as long as they have a 
    defined "__lt__" (<)-operator
    """
    length = len(list)

    for i in range(length):
        min_element_index = i

        for j in range (i, length):
            if list[j] < list[min_element_index]:
                min_element_index = j
        
        if min_element_index != i:
            list[i], list[min_element_index] = list[min_element_index], list[i]

    return list