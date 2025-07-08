import unittest
from katas.hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        
        self.assertEqual(hello_world(), "hello world")
