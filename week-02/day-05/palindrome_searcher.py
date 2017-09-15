main_palindrome = str(input('Please enter something: '))

def reverse(text):
    output = ""
    check_list = ""
    for i in range(len(text)-1, -1, -1):
        output += text[i]
    check_list = text + output
    return check_list


def palindrome_searcher(palindrome):
    palindrome1 = reverse(palindrome)
    for i in palindrome1:
        if i in range(len(palindrome)-1, -3) == i in range(len(palindrome1)-1, -3):
            print(i)
    



print(palindrome_searcher(main_palindrome))