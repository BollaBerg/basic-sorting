def insertionsort(list, descending=False):
    """
    Takes in a list as an argument, and sorts it using an "Insertion Sort"-algorithm.

    Has the following flags:
        - descending: Set True if sorting should be high-to-low. Default=False

    The list can be any length and contain any type of element, as long as they have a 
    defined "__lt__" (<)-operator.

    Insertion sort has a time complexity of O(n^2), but is considered one of the fastest algorithms for sorting
    very small lists. For more information, check out wikipedia: https://en.wikipedia.org/wiki/Insertion_sort
    """
    length = len(list)

    if descending:
        for count in range(1, length):
            temp_value = list[count]

            # Move all elements smaller than temp_value in list[0..count-1]
            # one step "up" / to the right in the array:
            j = count - 1
            while j >= 0 and list[j] < temp_value:
                list[j + 1] = list[j]
                j = j - 1
            
            # Set temp_value in at the right position in the array:
            list[j + 1] = temp_value

    else:   # Not descending, so must be ascending (low to high)
        for count in range(1, length):
            temp_value = list[count]

            # Move all elements greater than temp_value in list[0..count-1]
            # one step "up" / to the right in the array:
            j = count - 1
            while j >= 0 and temp_value < list[j]:
                list[j + 1] = list[j]
                j = j - 1
            
            # Set temp_value in at the right position in the array:
            list[j + 1] = temp_value

    return list