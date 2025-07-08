import unittest
from katas.hello_world import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
<<<<<<< HEAD
        #test
=======
        
>>>>>>> 8ba878a992da4a9765868416a660e5da0f9fe598
        self.assertEqual(hello_world(), "hello world")
