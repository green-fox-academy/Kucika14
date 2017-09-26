class Garden(object):
    def __init__(self, flower=2, tree=2):
        self.flower = flower
        self.tree = tree

class Flower(Garden):
    def __init__(self):
        super().__init__(flower)


