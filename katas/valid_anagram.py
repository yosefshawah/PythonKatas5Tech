def is_anagram(s1, s2):
    """
    Checks if two strings are anagrams of each other.
    An anagram is a word formed by rearranging the letters of another word.
    Case-insensitive and ignores spaces.

    Args:
        s1: the first string
        s2: the second string

    Returns:
        True if the strings are anagrams, False otherwise
    """
    return False


if __name__ == '__main__':
    test1 = ("listen", "silent")
    test2 = ("elbow", "below")
    test3 = ("study", "dusty")
    test4 = ("hello", "world")
    test5 = ("The Eyes", "They See")

    print(f'"{test1[0]}" and "{test1[1]}" are anagrams: {is_anagram(test1[0], test1[1])}')  # Should be True
    print(f'"{test2[0]}" and "{test2[1]}" are anagrams: {is_anagram(test2[0], test2[1])}')  # Should be True
    print(f'"{test3[0]}" and "{test3[1]}" are anagrams: {is_anagram(test3[0], test3[1])}')  # Should be True
    print(f'"{test4[0]}" and "{test4[1]}" are anagrams: {is_anagram(test4[0], test4[1])}')  # Should be False
    print(f'"{test5[0]}" and "{test5[1]}" are anagrams: {is_anagram(test5[0], test5[1])}')  # Should be True 