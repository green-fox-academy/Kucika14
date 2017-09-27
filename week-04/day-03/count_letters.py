class Counter(object):

    def count_letters(self, word):
        dictionary = {}
        for letter in word:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        return dictionary