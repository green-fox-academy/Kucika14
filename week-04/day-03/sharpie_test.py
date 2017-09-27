from sharpie import Sharpie
import unittest
my_dog = Sharpie('yellow', 10)
class SharpieTest(unittest.TestCase):

    def test_sharpe_use(self):
        my_dog.use()
        self.assertEqual(my_dog.ink_amount, 98.5)


if __name__ == '__main__':
    unittest.main()