import unittest

from katas.word_count import count_words  

class TestCountWords(unittest.TestCase):
    def test_normal_sentence(self):
        self.assertEqual(count_words("This is a sample sentence for counting words."), 8)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_multiple_spaces(self):
        self.assertEqual(count_words("This  is  spaced"), 3)

    def test_leading_trailing_spaces(self):
        self.assertEqual(count_words("  Leading and trailing  "), 3)

    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)

if __name__ == '__main__':
    unittest.main()
