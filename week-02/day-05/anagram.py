text1 = str(input('Please enter a word: '))
text2 = str(input('Please enter another one: '))

def is_anagram(test, original):
    if len(test) != len(original):
        return False
    for letter in test.lower():
        if letter not in original.lower():
            return False
    for letter in original.lower():
        if letter not in test.lower():
            return False
    return True

print(is_anagram(text1, text2))
