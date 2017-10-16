from random import randint

class Entities:
    def __init__(self, max_hp, dp, sp):
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.dp = dp
        self.sp = sp
        self.dice = self.dice_roll()

    def strike_entity(self, entity):
        if self.sp + self.dice_roll() > entity.dp:
            entity.current_hp -= self.dice_roll()

        if (entity.current_hp <= 0):
            print("krakk")
    

    def dice_roll(self):
        return randint(1,6)

class Hero(Entities):
    def __init__(self):
        super().__init__(20 + 3 * self.dice_roll(), 2*self.dice_roll(), 5+self.dice_roll())
        #super().__init__(20, 2, 5)
        self.xp = 0
        #self.dp = self.dp+2*self.dice_roll()
        #self.sp = self.sp+self.dice_roll()
        self.lvl = 1


class Skeleton(Entities):
    def __init__(self):
        super().__init__(200, 2, 5)
        print("skeleton")
        self.dp = self.dp
        self.sp = self.sp
        self.lvl = 1

class Boss(Entities):
    def __init__(self):
        super().__init__(200, 2, 5)
        self.dp = self.dp
        self.sp = self.sp
        self.lvl = 1

my_hero = Hero()