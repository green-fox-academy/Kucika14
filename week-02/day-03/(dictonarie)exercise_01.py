students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

# print(students[0]'candies'])
sum_candy = 0
def sum_of_candies(students):
    candy_counter = 0
    for student in students:
        candy_counter += student['candies']
    return candy_counter


def sum_of_people_that_has_less_than_5_candies(students):
    sum_of_ages = 0
    for student in students:
        if student["candies"] < 5:
            sum_of_ages += student["age"]
    return students

print(sum_of_people_that_has_less_than_5_candies(students))
# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies
