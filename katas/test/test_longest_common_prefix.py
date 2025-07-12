import unittest
from katas.longest_common_prefix import longest_common_prefix  # adjust the import path as needed

class TestLongestCommonPrefix(unittest.TestCase):

    def test_common_prefix_normal(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_full_match(self):
        self.assertEqual(longest_common_prefix(["test", "test", "test"]), "test")

    def test_partial_common_prefix(self):
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")

    def test_single_word(self):
        self.assertEqual(longest_common_prefix(["alone"]), "alone")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_common_prefix_one_letter(self):
        self.assertEqual(longest_common_prefix(["apple", "apricot", "ape"]), "ap")

    def test_mixed_length_words(self):
        self.assertEqual(longest_common_prefix(["a", "ab", "abc"]), "a")

    def test_one_empty_string(self):
        self.assertEqual(longest_common_prefix(["", "abc", "abcd"]), "")

    def test_all_empty_strings(self):
        self.assertEqual(longest_common_prefix(["", "", ""]), "")

if __name__ == '__main__':
    unittest.main()
