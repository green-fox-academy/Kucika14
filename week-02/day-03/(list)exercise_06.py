# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
chek_list = [4,8,12,16]
def checker(need_to_check, whole_list):
    for element in need_to_check:
        if not element in whole_list:
            return False
    return True


print(checker(chek_list, list_of_numbers))