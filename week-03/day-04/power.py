# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).


def powerer(base, power):
    if power == 1:
        return base
    else:
        return base * powerer(base,power -1)






print(powerer(3, 3))