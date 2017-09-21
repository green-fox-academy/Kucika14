# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.


def adder(num):
    if num <= 1:
        return num
    else:
        return adder(num -1) + num
        
print(adder(15))