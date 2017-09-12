# - Create a variable named `aj`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements in `aj`
# - Print the elements of the reversed `aj`

aj = [3, 4, 5, 6, 7]

def reverse(text):
    output = []
    for i in range(len(text)-1, -1, -1):
        output.append(text[i])
    return output

print(reverse(aj))