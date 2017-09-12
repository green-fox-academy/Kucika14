# - Create a function called `factorio`
#   that returns it's input's factorial
number = int(input('pls enter a number: '))
def factorio(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

print(factorio(number))