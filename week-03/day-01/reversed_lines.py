# Create a method that decrypts reversed-lines.txt
def decrypt(file_name):
    with open(file, "r") as file1:
        for line in file1:
            print(line[::-1])







file = 'E:/greenfox/Kucika14/week-03/day-01/reversed_lines.txt'
decrypt(file)