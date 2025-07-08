def find_missing_number(numbers):
    """
    Finds the missing number in a list that should contain consecutive integers
    from 0 to n, where one number is missing.

    Args:
        numbers: the list of integers with one missing number

    Returns:
        the missing number
    """
    return 0


if __name__ == '__main__':
    test1 = [3, 0, 1]  # Missing 2
    test2 = [0, 1, 3, 4, 5]  # Missing 2
    test3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # Missing 8
    test4 = [1, 2, 3, 4, 5]  # Missing 0

    print(f"Missing number in {test1}: {find_missing_number(test1)}")  # Should be 2
    print(f"Missing number in {test2}: {find_missing_number(test2)}")  # Should be 2
    print(f"Missing number in {test3}: {find_missing_number(test3)}")  # Should be 8
    print(f"Missing number in {test4}: {find_missing_number(test4)}")  # Should be 0 