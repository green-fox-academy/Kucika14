# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#1234567
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
number = int(input('pls enter a number: '))
output = "*"
for i in range(1,number+1):
    output = output * i
    print(output)
    output = "*"