def mergesort(list, descending=False):
    """
    Takes in a list as an argument, and sorts it using a "Merge Sort"-algorithm.

    ---

    Has the following flags:

        - descending: Set True if sorting should be high-to-low. Default=False

    ---

    The list can be any length and contain any type of element, as long as they have a 
    defined "__lt__" (<)-operator.

    Insertion sort has a time complexity of O(n log n). It is a stable sort, and is efficient at handling
    slower media. It is perfect for linked lists.
    For more information, check out wikipedia: https://en.wikipedia.org/wiki/Merge_sort
    """
    length = len(list)
    if length <= 1:
        return list
    else:
        midpoint = length // 2

    if descending:
        # Split list:
        left_side = list[:midpoint]
        right_side = list[midpoint:]

        # Recursively sort left and right side
        mergesort(left_side, descending=descending)
        mergesort(right_side, descending=descending)

        # Empty starting list
        list.clear()

        # Compare every element in left- and right side. Add the highest element to list
        # If two elements are equal, add the one from right_side first (to ensure stable sort)
        while len(left_side) > 0 and len(right_side) > 0:
            if right_side[0] < left_side[0]:
                list.append(left_side[0])
                left_side.pop(0)
            else:
                list.append(right_side[0])
                right_side.pop(0)

        # Go through all leftover (or rightover if right_side :P) elements and add to list
        for leftover_element in left_side:
            list.append(leftover_element)
        for rightover_element in right_side:
            list.append(rightover_element)

    else:   # Not descending, so must be ascending (low to high)
        # Split list:
        left_side = list[:midpoint]
        right_side = list[midpoint:]

        # Recursively sort left and right side
        mergesort(left_side, descending=descending)
        mergesort(right_side, descending=descending)

        # Empty starting list
        list.clear()

        # Compare every element in left- and right side. Add the lowest element to list
        # If two elements are equal, add the one from left_side first (to ensure stable sort)
        while len(left_side) > 0 and len(right_side) > 0:
            if right_side[0] < left_side[0]:
                list.append(right_side[0])
                right_side.pop(0)
            else:
                list.append(left_side[0])
                left_side.pop(0)

        # Go through all leftover (or rightover if right_side :P) elements and add to list
        for leftover_element in left_side:
            list.append(leftover_element)
        for rightover_element in right_side:
            list.append(rightover_element)

    return list