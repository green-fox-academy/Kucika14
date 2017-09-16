
def palindrome(letters):
        if letters == letters[::-1]:
            return True
        return False

def bruteForceSearch(letters):
    palindoromeList = [] 
    for i in range(0, len(letters) - 2):
        for j in range(i + 2, len(letters)):
            candidate = letters[i:j + 1]
            if palindrome(candidate):
                palindoromeList.append(candidate)

    return palindoromeList

def __main():
    sentence = str(input('pls enter something: '))

    # palindrome(sentence)
    print(bruteForceSearch(sentence))


__main()