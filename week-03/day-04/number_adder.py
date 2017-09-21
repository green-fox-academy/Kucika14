# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.


def adder(num):
    if num <= 1:
        return num
    else:
        print(num)
        return adder(num -1)+adder(num -2)
        
print(adder(10))