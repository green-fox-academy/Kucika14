class Sharpie(object):
    def __init__(self, color, width, ink_amount=100):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount


    def use(self):
        self.ink_amount -= 1.5


dog  = Sharpie("yellow", 10)
dog.use()
print(dog.ink_amount)
