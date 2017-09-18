def divide(number):
    try:
        print(10 / number)
    except ZeroDivisionError:
        print('Can\'t divide by zero!')

number = int(input('enter a number pls: '))
divide(number)