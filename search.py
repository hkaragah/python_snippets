def binary_search(sorted_list: list[float], target: float) -> int:
    """Search for target within a sorted list using binary algorithm,
        if found returnt the index, otherwise return -1.
        If there are multiple occurece, the algorithm may find any of them.
        There is no garantee to find the first or last occurence.

    Args:
        sorted_list (list): sorted list of elements
        target (float): element to search for in sorted_list

    Returns:
        int: if target found in sorted_list, index of target within sprted_list, otherwise -1
    """
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


def binary_search_first_occurence(sorted_list: list[float], target: float) -> int:
    """Search for target within a sorted list using binary algorithm,
        if found returnt the index, otherwise return -1.
        If there are repeated elements, it returns the index of the first occurence.

    Args:
        sorted_list (list): sorted list of elements
        target (float): element to search for in sorted_list

    Returns:
        int: if target found in sorted_list as its first occurence, index of target within sprted_list, otherwise -1
    """
    left = 0
    right = len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] > target:
            right = mid - 1
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            if mid == 0 or sorted_list[mid - 1] != target: # first occurence
                return mid
            else:
                right = mid - 1
            
    return -1



def linearSearch(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
    return -1