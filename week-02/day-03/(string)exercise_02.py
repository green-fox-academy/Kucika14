# Create a function called 'reverse_string' which takes a string as a parameter
# The function reverses it and returns with the reversed string


reversed_string = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"


def reverse_string(text):
    output = ''
    for i in range(len(text)-1, -1, -1):
        output = output + text[i]
    return output

print(reverse_string(reversed_string))