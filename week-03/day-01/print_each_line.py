try:
    my_file = open("my lines.txt", "w")
    print(my_file.read())
except IOError:
    print("Unable to read file: my-file.txt")