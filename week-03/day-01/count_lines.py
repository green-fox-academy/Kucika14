# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.



def stringPrinter(string):
    try:
        string = open(my_file, "r")
        for line in string:
            print(line)
    except:
        print("0")





my_file = "my_file.txt"
stringPrinter(my_file)