# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs the farmer has
# It should print how many legs all the animals have
print('How many chicken you have?')
chicken = int(input())
print('How many pig you have?')
pig = int(input())
print('Than you have ' + str(chicken + pig) + ' animals and they have ' + str(chicken*2 + pig*4) + ' legs together.' )