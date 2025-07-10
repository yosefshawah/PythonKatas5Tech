import unittest
from katas.is_unique_str import is_unique  

class TestIsUnique(unittest.TestCase):
    def test_repeated_chars(self):
        self.assertFalse(is_unique("Hello"))  # 'l' repeats (case-insensitive)

    def test_all_unique(self):
        self.assertTrue(is_unique("World"))
        self.assertTrue(is_unique("Python"))
     
      

    def test_empty_string(self):
        self.assertTrue(is_unique(""))

    def test_case_insensitive(self):
        self.assertFalse(is_unique("Aa"))  # 'A' and 'a' same char ignoring case

    def test_special_chars(self):
        self.assertTrue(is_unique("!@#$%^&*()"))
        self.assertFalse(is_unique("!@#!!"))  # '!' repeats

if __name__ == '__main__':
    unittest.main()
