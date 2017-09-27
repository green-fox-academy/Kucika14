class Aircraft(object):
    def __init__(self, plane1):
        self.plane1 = plane1
        if plane1 == 'F16':
            max_ammo = 8
            base_dmg = 30
            ammo = 0
        elif plane1 == 'F35':
            max_ammo = 12
            base_dmg = 50
            ammo = 0

    def fight(self):
        self.dmg_dealt = self.ammo*self.base_dmg
        self.ammo = 0
        return self.dmg_dealt
    
    def refill(self, number):
        self.fill_ammo = number
        self.current_ammo = self.max_ammo
        return number - self.max_ammo

