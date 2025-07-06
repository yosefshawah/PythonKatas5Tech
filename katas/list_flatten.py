def flatten_list(nested_list):
    """
    Flattens a nested list into a single list of integers.

    Args:
        nested_list: the input nested list

    Returns:
        a flat list containing all integers from the nested structure
    """
    # hint: isinstance()
    return []


if __name__ == '__main__':
    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]