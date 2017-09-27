from apple import Apples
import unittest

class AppleTest(unittest.TestCase):

    def test_apple_is_string(self):
        my_apple = Apples()
        self.assertEqual(my_apple.get_apple(), "apple")

    def test_apple_is_string(self):
        my_apple = Apples()
        self.assertEqual(my_apple.get_apple("pig"), "pig")


if __name__ == '__main__':
    unittest.main()