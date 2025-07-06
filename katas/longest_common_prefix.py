def longest_common_prefix(strs):
    """
    Finds the longest common prefix in a list of strings.

    Args:
        strs: the list of strings

    Returns:
        the longest common prefix, or an empty string if none exists
    """
    return ""


if __name__ == '__main__':
    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["interspecies", "interstellar", "interstate"]
    test4 = ["apple", "apricot", "ape"]

    print(f"Longest Common Prefix: {longest_common_prefix(test1)}")  # Output: "fl"
    print(f"Longest Common Prefix: {longest_common_prefix(test2)}")  # Output: ""
    print(f"Longest Common Prefix: {longest_common_prefix(test3)}")  # Output: "inter"
    print(f"Longest Common Prefix: {longest_common_prefix(test4)}")  # Output: "ap"