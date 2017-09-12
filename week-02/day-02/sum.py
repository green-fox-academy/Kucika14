# - Write a function called `sum` that sum all the numbers
#   until the given parameter
 
number = int(input('pls enter a number: '))
def main_sum(a):
    return sum(list(range(1, a + 1)))

print(main_sum(number))
