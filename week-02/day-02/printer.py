# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

user_input = input('pls enter something: ')
user_input2 = input('pls enter something: ')

def printer(a, b):
    print(a + " " + b)

printer(user_input , user_input2)
