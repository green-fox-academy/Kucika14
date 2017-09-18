# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful

def copy(filename):
    try:
        f1 = open(filename, "r")
        f2 = f1.read()
        copied_file = open('copied-file.txt', "w")
        copied_file.write(f2)
        copied_file.close
        copied_file = open('copied-file.txt', 'r')
        f3 = copied_file.read()
        print(f2 == f3)
    except:
        print('try again')



file = "E:\greenfox\Kucika14\week-03\day-01\my-file.txt"
copy(file)