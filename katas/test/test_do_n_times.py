import unittest
from unittest.mock import Mock
<<<<<<< HEAD
from katas.do_n_times import do_n_times  
=======
from katas.do_n_times import do_n_times  # Replace with the actual module name
>>>>>>> f868093 (test for n_times and is_unique)

class TestDoNTimes(unittest.TestCase):
    def test_do_n_times_called_exact_number(self):
        mock_func = Mock()

        do_n_times(mock_func, 5)
        self.assertEqual(mock_func.call_count, 5)

        do_n_times(mock_func, 0)
        self.assertEqual(mock_func.call_count, 5)  # No change

        do_n_times(mock_func, 2)
        self.assertEqual(mock_func.call_count, 7)

    def test_do_n_times_with_negative(self):
        mock_func = Mock()
        do_n_times(mock_func, -3)  # should not raise or call
        self.assertEqual(mock_func.call_count, 0)

if __name__ == '__main__':
    unittest.main()
