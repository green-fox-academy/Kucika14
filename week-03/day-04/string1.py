# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.


def string(text):
    if len(text) == 0:
        return text
    elif text[0] == "x":
        return "y" + string(text[1:])
    else:
        return text[0] + string(text[1:])


print(string("fux kex box"))