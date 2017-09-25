import random

class Pirates(object):
    def __init__(self, name):
        self.name = name
        self.how_much_rum = 0
        self.alive = True
        


    def drink_some_rum(self):
        if self.alive == False:
            print("He is dead.")
        self.how_much_rum += 1
        print(self.name + " had " + str(self.how_much_rum) + " rum.")
        if self.how_much_rum > 4:
            self.koncked_out()



    def hows_it_going_mate(self):
        if self.alive == False:
            print("He is dead.")
        elif self.how_much_rum < 5:
            print("Pour me anudder!")
        elif self.drink_some_rum >= 5:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            self.koncked_out
        elif self.how_much_rum >  7:
            self.koncked_out 

        

    def koncked_out(self):
        print(str(self.name) + ", the pirate passes out and sleeps it off.")
        self.how_much_rum = 0

    def die(self):
        self.alive = False

    def brawl(self,pirate):
        if self.alive == False or pirate.alive == False:
            print("You cant fight with a dead man.")
        else:
            dice1 = self.dice_check()
            dice2 = pirate.dice_check()
            if dice1 == 1:
                self.die()
                print(str(self.name)+ " lost his life.")
            elif dice2 == 1:
                pirate.die()
                print(str(pirate.name)+ " lost his life.")
            else:
                print("no-one died")
        

    def dice_check():
        dice = random.randint(1,3)
        return dice

class Parrot(object):

    def __init__(self, name):
        self.name = name


class Ship(object):


    def __init__(self, crew):
        self.crew = [crew]

    def __repr__(self):
        return '[{}]'.format(self.crew)

    def crew_members():
        crew = []
        crew.append(Fred)
        crew.append(Jimmy)
        crew.append(Roger)
        crew.append(Wade)
        crew.append(Jack)
        crew.append(Bill)
        crew.append(Larry)
        return crew

crew = crew_members()

Fred = Pirates('Fred')
Jimmy = Pirates('Jimmy')
Roger = Pirates('Roger')
Wade = Pirates('Wade')
Jack = Pirates('Jack')
Bill = Pirates('Bill')
Larry = Pirates('Larry')
cocain = Parrot('Cocain')

Jack.drink_some_rum()
Jack.drink_some_rum()
Jack.drink_some_rum()

print(Jack.brawl(Bill))
