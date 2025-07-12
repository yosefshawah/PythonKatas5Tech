import unittest
from katas.true_counter import count_true_values  

class TestCountTrueValues(unittest.TestCase):
    def test_mixed_values(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)

    def test_all_true(self):
        self.assertEqual(count_true_values([True, True, True]), 3)

    def test_all_false(self):
        self.assertEqual(count_true_values([False, False, False]), 0)

    def test_empty_list(self):
        self.assertEqual(count_true_values([]), 0)

    def test_non_boolean_values(self):
        # Should ignore truthy non-boolean values if checking is strict with `is True`
        self.assertEqual(count_true_values([1, 0, "True", True, False]), 1)

    def test_boolean_like_values(self):
        # If code checks `item == True` (not `is True`), 1 would be included — but yours uses `is True`, so only strict True
        self.assertEqual(count_true_values([True, 1, True, 0]), 2)

if __name__ == '__main__':
    unittest.main()
