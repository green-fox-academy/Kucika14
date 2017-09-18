try:
    my_file = open("my-file.txt", "r")
    for line in my_file:
        print(line)
except IOError:
    print("Unable to read file: my-file.txt")