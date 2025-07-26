import unittest

from katas.valid_anagram import is_anagram 

class TestIsAnagram(unittest.TestCase):

    def test_basic_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("elbow", "below"))
        self.assertTrue(is_anagram("study", "dusty"))

    def test_not_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("test", "tess"))

    def test_case_insensitive(self):
        self.assertTrue(is_anagram("State", "Taste"))

    def test_ignores_spaces(self):
        self.assertTrue(is_anagram("The Eyes", "They See"))
        self.assertTrue(is_anagram("Conversation", "Voices Rant On"))
        self.assertFalse(is_anagram("Listen ", " Silent"))  # Spaces at ends still ignored

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", ""))

if __name__ == '__main__':
    unittest.main()
