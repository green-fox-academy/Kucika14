class Anagramma(object):

    def compare_anagram(self, string):
        if string == string[::-1]:
            return True
        return False
