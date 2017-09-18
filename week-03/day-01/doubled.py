# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    file_name = open(file, "r")
    decrypted_file = open('decrypted-file.txt', "w")
    for each in file_name:
        dup_char = ""
        dup_char += each[::2]
        decrypted_file.write(dup_char)
    decrypted_file.close
    file_name.close





file = 'E:\greenfox\Kucika14\week-03\day-01\doubled.txt'
decrypt(file)