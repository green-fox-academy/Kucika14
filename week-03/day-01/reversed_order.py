

def decrypt(file_name):
    line_list = []
    with open(file, "r") as file1:
        for line in file1:
            line_list.append(line)
    for i in line_list[::-1]:
        print(i)







file = 'E:/greenfox/Kucika14/week-03/day-01/reversed_order.txt'
decrypt(file)