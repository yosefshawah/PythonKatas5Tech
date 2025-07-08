import unittest
from katas.list_diff import find_difference


class TestListDiff(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_difference("string")
    def test_list_diff_true(self):
        self.assertEqual(find_difference( [10, 3, 5, 6, 40, -2]), 42)

    def test_list_diff_isEmpty(self):
        with self.assertRaises(ValueError):
            find_difference([])