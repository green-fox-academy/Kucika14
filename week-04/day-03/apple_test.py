from apple import Apples
import unittest

my_apple = Apples()

class AppleTest(unittest.TestCase):

    def test_apple_is_string1(self):
        self.assertEqual(my_apple.get_apple('apple'), 'apple')

    def test_apple_is_string2(self):
        self.assertEqual(my_apple.get_apple('pig'), 'pig')


if __name__ == '__main__':
    unittest.main()