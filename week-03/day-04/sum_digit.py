# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 // 10 is 12).


def sum_digits(num):
    if num == 0:
        return num
    else:
        return num%10 + sum_digits(num//10)




print(sum_digits(3546))