# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def string(text):
    text2 = ""
    if len(text) == 1:
        return text2 + text[0]
    else:
        text2 = text2 + text[0] + "*"
        return text2 + string(text[1:])


print(string("fux kex box"))