# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
number = int(input('pls enter a number: '))
output = "*"
sapce = " "
for i in range(1,number+1):
    space = space * i
    output = output * i
    print(output)
    output = "*"