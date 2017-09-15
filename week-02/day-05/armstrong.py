number = input('Pls enter a number: ')

sum_number = 0
digit = 0
for i in range(len(number)):
    digit = int(number[i])
    sum_number = sum_number + digit ** len(number)
if sum_number == int(number):
    print(str(number) + " is an Armstrong number")
else:
    print(str(number) + " is NOT an Armstrong number")