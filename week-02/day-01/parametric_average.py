# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4


number = int(input('pls enter a number: '))
number1 = int(input('pls enter a second one: '))
number2 = int(input('...and a third one :) : '))

summ = number + number1 + number2
average = summ / 3

print(summ, average)