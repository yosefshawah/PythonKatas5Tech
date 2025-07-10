import unittest
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f868093 (test for n_times and is_unique)
from katas.is_unique_str import is_unique  # Replace with your module name or just import if in same file

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
<<<<<<< HEAD
=======
from katas.is_unique_str import is_unique


class TestIsUnique(unittest.TestCase):
    def test_empty_str(self):
        self.assertEqual(is_unique(''), True)

    def test_unique(self):
        self.assertEqual(is_unique('word'), True)

    def test_not_unique(self):
        self.assertEqual(is_unique('aaa'), False)

    def test_unique_case_insensitivity(self):
        self.assertEqual(is_unique('Aa'), True)

>>>>>>> 8ba878a992da4a9765868416a660e5da0f9fe598
=======
>>>>>>> f868093 (test for n_times and is_unique)
