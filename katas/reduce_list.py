def reduce_array(numbers):
    """
    Modifies the list so that each element becomes the difference between
    itself and its predecessor. The first element remains unchanged.

    Args:
        numbers: the list of integers to modify
    """
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i] - numbers[i - 1]
    return numbers


def print_list(array):
    """
    Helper function to print the elements of a list.

    Args:
        array: the list to print
    """
    print(' '.join(str(num) for num in array))


if __name__ == '__main__':
    sample_list = [10, 15, 7, 20, 25]
    print("Original list: ")
    print_list(sample_list)
    reduce_array(sample_list)
    print("Reduced list: ")
    print_list(sample_list)

    # Expected output:
    # Original list:
    # 10 15 7 20 25
    # Reduced list:
    # 10 5 -8 13 5