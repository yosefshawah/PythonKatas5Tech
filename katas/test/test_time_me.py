import unittest
import time
from katas.time_me import measure_execution_time

def sample_function():
    """A function that sleeps for 500ms."""
    time.sleep(0.5)

def quick_function():
    """A function that performs a quick task."""
    pass  # no print here to avoid noise during testing

class TestMeasureExecutionTime(unittest.TestCase):
    def test_sample_function_timing(self):
        """Check that sample_function takes ~500ms (allowing some margin)."""
        duration = measure_execution_time(sample_function)
        self.assertGreaterEqual(duration, 450)
        self.assertLessEqual(duration, 600)

    def test_quick_function_timing(self):
        """Check that quick_function is very fast (under 50ms)."""
        duration = measure_execution_time(quick_function)
        self.assertLess(duration, 50)

if __name__ == '__main__':
    unittest.main()
