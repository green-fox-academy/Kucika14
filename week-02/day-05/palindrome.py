palindrome = str(input('Please enter something: '))

def reverse(text):
    output = ""
    for i in range(len(text)-1, -1, -1):
        output += text[i]
    print(palindrome + output)


reverse(palindrome)