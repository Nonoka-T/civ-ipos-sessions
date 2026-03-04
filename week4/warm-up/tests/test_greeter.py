import unittest
from src.greeter import greet

class TestGreeter(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), 'Hello John')

if __name__ == "__main__":
    unittest.main()