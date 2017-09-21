# Given a string, compute recursively a new string where all the 'x' chars have been removed.



def string(text):
    if len(text) == 0:
        return text
    elif text[0] == "x":
        return "" + string(text[1:])
    else:
        return text[0] + string(text[1:])


print(string("fux kex box jax fax kox buxa xilofon"))