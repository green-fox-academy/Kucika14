from fibonacci import Fibonacci
import unittest

my_fibo = Fibonacci()

class FibonacciTest(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(my_fibo.fibonacci(4), 3)


if __name__ == '__main__':
    unittest.main()