from count_letters import Counter
import unittest
my_word = Counter()
class AnagramTest(unittest.TestCase):

    def test_empty_letters(self):
        self.assertEqual(my_word.count_letters(""), {})

    def test_one_letters(self):
        self.assertEqual(my_word.count_letters('a'), {'a':1})

    def test_two_letters(self):
        self.assertEqual(my_word.count_letters('ab'), {'a':1, 'b':1})

    def test_same_letters(self):
        self.assertEqual(my_word.count_letters('aa'), {'a':2})



if __name__ == '__main__':
    unittest.main()