from anagram import Anagramma
import unittest
my_text = Anagramma()
class AnagramTest(unittest.TestCase):

    def test_anagram_true(self):
        self.assertEqual(my_text.compare_anagram('indulagorogaludni'), True)


    def test_anagram_false(self):
        self.assertEqual(my_text.compare_anagram('burgonya'),False)


    def test_second_anagram_true(self):
        self.assertEqual(my_text.compare_anagram('gezakekazeg'),True)


    def test_second_anagram_false1(self):
        self.assertEqual(my_text.compare_anagram('Kecske'),False)


if __name__ == '__main__':
    unittest.main()