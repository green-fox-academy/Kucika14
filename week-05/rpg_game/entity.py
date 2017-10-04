
class Entities:
    def __init__(self):
        self.max_hp = max_hp
        self.currnet_hp = currnet_hp
        self.dp = dp
        self.sp = sp

class Hero(Entities):
    def __init__(self):
        super().__init__(20, 20, 2, 5)
        self.xp = 0




class Skeleton:
    def __init__(self):
        super().__init__(20, 20, 2, 5)

class Boss:
    def __init__(self):
        super().__init__(20, 20, 2, 5)