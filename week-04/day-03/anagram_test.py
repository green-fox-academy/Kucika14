from anagram import Anagramma
import unittest
my_text = Anagramma()
class AnagramTest(unittest.TestCase):

    def test_anagram_true(self):
        self.assertTrue(my_text.compare_anagram('oro'), 'oro')

    def test_anagram_false(self):
        self.assertTrue(my_text.compare_anagram('oro'), 'kecske')

if __name__ == '__main__':
    unittest.main()