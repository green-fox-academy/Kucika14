# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
number = int(input('pls enter a number: '))
output = "%"
space = " "
for i in range(1,number+1):
    output = number * output
    space = number * (i + 1)
    print(output)
    output = "%"
    space = " "