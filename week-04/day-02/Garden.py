class Garden(object):
    def __init__(self, flower, tree):
        self.flower = flower
        self.tree = tree
        
    def water_lvl_check(self, flower_water_lvl, tree_water_lvl):
        if flower_water_lvl < 5 or tree_water_lvl < 10:
            watering_plants()
        else:
            flower_water_lvl() or tree_water_lvl

    def watering_plants(self):
        self.water += 3

class Flower(Garden):
    def __init__(self, color):
        self.color = color
        self.water = 1

    def flower_water_lvl(self):
        if self.water <= 5:
            print('The ' + self.color + ' flower needs water')
        else:
            print('This ' + self.color + ' flower is feeling good right now')


class Tree(Garden):
    def __init__(self, color):
        self.color = color
        self.water = 10

    def tree_water_lvl(self):
        if self.water <= 10:
            print('The ' + self.color + ' tree needs water')
        else:
            print('This ' + self.color + ' tree is feeling good right now')


flower = Flower('yellow')
flower2 = Flower('pink')
flower2.flower_water_lvl()
flower2.watering_plants()
flower2.watering_plants()
flower2.watering_plants()
flower2.flower_water_lvl()

