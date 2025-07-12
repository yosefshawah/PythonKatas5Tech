import unittest
from katas.sum_of_digits import sum_of_digits  

class TestSumOfDigits(unittest.TestCase):
    def test_only_digits(self):
        self.assertEqual(sum_of_digits("12345"), 15)

    def test_mixed_characters(self):
        self.assertEqual(sum_of_digits("abc123"), 6)
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)

    def test_no_digits(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)

    def test_empty_string(self):
        self.assertEqual(sum_of_digits(""), 0)

    def test_all_non_digit_ascii(self):
        self.assertEqual(sum_of_digits("abcXYZ!@#"), 0)

    def test_digits_with_spaces(self):
        self.assertEqual(sum_of_digits("1 2 3 4 5"), 15)

    def test_zeroes(self):
        self.assertEqual(sum_of_digits("000"), 0)

if __name__ == '__main__':
    unittest.main()
