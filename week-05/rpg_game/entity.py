from random import randint

class Entities:
    def __init__(self, max_hp, dp, sp):
        self.max_hp = max_hp
        self.currnet_hp = currnet_hp
        self.dp = dp
        self.sp = sp
        self.dice = self.dice_roll()

    def dice_roll(self):
        return randint(1,6)

class Hero(Entities):
    def __init__(self):
        super().__init__(20, 2 )
        self.xp = 0
        self.dp =




class Skeleton:
    def __init__(self):
        super().__init__(2, 2, 5)

class Boss:
    def __init__(self):
        super().__init__(20, 2, 5)