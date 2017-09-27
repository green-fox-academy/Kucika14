from sum import Summary
import unittest
my_sum = Summary()

class SumTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(my_sum.summ([1,2,3]), 6)

    def test_empty_sum(self):
        self.assertEqual(my_sum.summ([]), 0)
    
    def test_one_element_sum(self):
        self.assertEqual(my_sum.summ([1]), 1)

    def test_with_null(self):
        self.assertEqual(my_sum.summ(None), None)



if __name__ == '__main__':
    unittest.main()