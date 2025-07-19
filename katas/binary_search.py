def binary_search(sorted_array, target):
    """
    Performs binary search on a sorted array to find the target value.

    Time complexity: O(log n)
    Space complexity: O(1)

    Args:
        sorted_array: the sorted list of integers
        target: the value to search for

    Returns:
        the index of the target value if found, or -1 if not found
    """
    return -1


if __name__ == '__main__':
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print(binary_search(test_array, 7))  # Should be 3
    print(binary_search(test_array, 8))  # Should be -1 