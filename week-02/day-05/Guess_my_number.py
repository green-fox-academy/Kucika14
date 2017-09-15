import random

map_range = int(input('Enter a number wich you want in play: '))

def game(max_range):
    lives = int(input('How many lives do u want?: '))
    magic_number = random.randint(1, map_range)
    guess = int(input('Pls enter your guess number: '))
    while guess != magic_number and lives > 0:
        print('guess again')
        lives -= 1
        print('You have lost one life! You have just ' + str(lives) + ' left!')
        if lives == 0:
            print('No more lives! Game Over! :(')
        elif guess < magic_number:
            guess = int(input('More! Try again: '))
        else:
            guess = int(input('less! Try aigan: '))
    if guess == magic_number:
        print('congrat')


game(map_range)