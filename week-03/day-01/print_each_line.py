try:
    my_file = open("my lines.txt", "r")
    for line in my_file:
        print(my_file.readline())
        my_file.close
except IOError:
    print("Unable to read file: my-file.txt")