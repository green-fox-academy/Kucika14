# Write a program that reads a number form the standard input,
# Than prints "Odd" if the number is odd, or "Even" it it is even.

number = int(input('Enter a number pls: '))

if number % 2 ==0 and number !=0:
    print('Your number is even')
else:
    print('Your number is odd')
