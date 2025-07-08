import unittest
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

