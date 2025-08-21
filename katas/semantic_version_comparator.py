def compare_versions(version1, version2):
    """
    Compares two semantic version strings to determine their relative order.

    Semantic versioning follows the format "MAJOR.MINOR.PATCH" where:
    - MAJOR version increments for incompatible API changes
    - MINOR version increments for backward-compatible functionality
    - PATCH version increments for backward-compatible bug fixes

    Each component must be compared numerically, not lexicographically.

    Args:
        version1: the first version string (e.g., "MAJOR.MINOR.PATCH")
        version2: the second version string (e.g., "MAJOR.MINOR.PATCH")

    Returns:
        -1 if version1 < version2
         0 if version1 = version2
         1 if version1 > version2
    """
    # Split and convert to integers
    parts1 = list(map(int, version1.split("."))) # map() is used to apply a function to each element of an iterable
    parts2 = list(map(int, version2.split(".")))

    # Pad shorter list with zeros
    max_len = max(len(parts1), len(parts2))
    parts1.extend([0] * (max_len - len(parts1))) # extend() is used to add elements to the end of a list
    parts2.extend([0] * (max_len - len(parts2)))

    # Compare component by component
    for p1, p2 in zip(parts1, parts2): # zip() is used to iterate over two lists simultaneously
        if p1 < p2:
            return -1
        elif p1 > p2:
            return 1
    return 0
    
    


if __name__ == '__main__':
    print(f"'1.0.0' compared to '1.0.1': {compare_versions('1.0.0', '1.0.1')}")  # Expected: -1
    print(f"'2.1.0' compared to '1.9.9': {compare_versions('2.1.0', '1.9.9')}")  # Expected: 1
    print(f"'1.2.3' compared to '1.2.3': {compare_versions('1.2.3', '1.2.3')}")  # Expected: 0

    # Additional test cases
    print(f"'1.2' compared to '1.2.0': {compare_versions('1.2', '1.2.0')}")  # Expected: 0
    print(f"'1.10.0' compared to '1.2.0': {compare_versions('1.10.0', '1.2.0')}")  # Expected: 1
    print(f"'2.0.0' compared to '10.0.0': {compare_versions('2.0.0', '10.0.0')}")  # Expected: -1