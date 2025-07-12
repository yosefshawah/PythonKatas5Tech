def longest_common_prefix(strs):
    """
    Finds the longest common prefix in a list of strings.

    Args:
        strs: the list of strings

    Returns:
        the longest common prefix, or an empty string if none exists
    """
    def starts_with(word, prefix):
        if len(prefix) > len(word):
            return False
        for i in range(len(prefix)):
            if word[i] != prefix[i]:
                return False
        return True

    
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        while not starts_with(word, prefix):
            prefix = prefix[:-1]  # chop one character at a time
            if not prefix:
                return ""

    return prefix


if __name__ == '__main__':
    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["interspecies", "interstellar", "interstate"]
    test4 = ["apple", "apricot", "ape"]

    print(f"Longest Common Prefix: {longest_common_prefix(test1)}")  # Output: "fl"
    print(f"Longest Common Prefix: {longest_common_prefix(test2)}")  # Output: ""
    print(f"Longest Common Prefix: {longest_common_prefix(test3)}")  # Output: "inter"
    print(f"Longest Common Prefix: {longest_common_prefix(test4)}")  # Output: "ap"