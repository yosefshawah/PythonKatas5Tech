import time


def measure_execution_time(func):
    """
    Measures the time it takes to execute a given function.

    Args:
        func: the function to measure

    Returns:
        the execution time in milliseconds
    """
    # hint: time.time()
    return 0


def sample_function():
    """A function that sleeps for 500ms."""
    time.sleep(0.5)


def quick_function():
    """A function that performs a quick task."""
    print("Quick task done!")


if __name__ == '__main__':
    time_taken = measure_execution_time(sample_function)
    print(f"Time taken by sample_function: {time_taken} ms")

    time_taken = measure_execution_time(quick_function)
    print(f"Time taken by quick_function: {time_taken} ms")

    # Expected output:
    # Time taken by sample_function: ~500 ms
    # Quick task done!
    # Time taken by quick_function: < 1 ms