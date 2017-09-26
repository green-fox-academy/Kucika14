class Garden(object):
    def __init__(self):
        self.plants = []

    def plant_append(self, plant):
        self.plants.append(plant)
        
    def water_lvl_check(self, flower_water_lvl, tree_water_lvl):
        if flower_water_lvl < 5 or tree_water_lvl < 10:
            watering_plants()
        else:
            flower_water_lvl() or tree_water_lvl

    def watering_plants(self):        
        for plant in self.plants:
            if isinstance(plant,Flower):
                plant.water += 10*0.75
            elif isinstance(plant,Tree):
                plant.water += 10*0.4
            plant.water_lvl()

class Plant(object):
    def __init__(self, color):
        self.water = 0
    

class Tree(Plant):
    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def water_lvl(self):
        if self.water <= 5:
            print('The ' + self.color + ' tree needs water')

        else:
            print('This ' + self.color + ' tree is feeling good right now')


class Flower(Plant):
    def __init__(self, color):
        super().__init__(color)
        self.color = color


    def water_lvl(self):
        if self.water <= 10:
            print('The ' + self.color + ' flower needs water')
        else:
            print('This ' + self.color + ' flower is feeling good right now')



flower = Flower('yellow')
flower1 = Flower('blue')
flower2 = Flower('pink')
tree = Tree('Purple')
tree1 = Tree('orange')
tree2 = Tree('red')
my_garden = Garden()
my_garden.plant_append(flower)
my_garden.plant_append(flower1)
my_garden.plant_append(flower2)
my_garden.plant_append(tree)
my_garden.plant_append(tree1)
my_garden.plant_append(tree2)
my_garden.watering_plants()
my_garden.watering_plants()
my_garden.watering_plants()

# print(plant.plants[0].color)

