import unittest
from katas.true_counter import count_true_values  

class TestCountTrueValues(unittest.TestCase):
    def test_mixed_true_false(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)

    def test_all_true(self):
        self.assertEqual(count_true_values([True, True, True]), 3)

    def test_all_false(self):
        self.assertEqual(count_true_values([False, False]), 0)

    def test_empty_list(self):
        self.assertEqual(count_true_values([]), 0)

    def test_non_boolean_values(self):
        # If input has non-bool but truthy/falsy values, only True (bool) counts
        self.assertEqual(count_true_values([True, 1, 0, False, "True", None]), 1)

if __name__ == '__main__':
    unittest.main()
