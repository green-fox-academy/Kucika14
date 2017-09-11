# Write a program that asks for two numbers
# Thw first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people
girl=int(input('How many girls are there?: '))
boy=int(input('How many boys are there?: '))

if girl == boy and girl+boy >= 20:
    print('The party is exellent!')
elif girl <= 0:
    print('Sausage party')
elif girl+boy >= 20:
    print('Quite cool party!')
elif girl+boy < 20:
    print('Average party...')
else:
    print('Where the hell are you?!?!?')