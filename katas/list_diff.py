def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    if not isinstance(numbers, list):
        raise TypeError("Expected a list")
    
    if len(numbers) == 0:
        raise ValueError("Invalid value, expected at least 2 numbers")

    return max(numbers) - min(numbers)
