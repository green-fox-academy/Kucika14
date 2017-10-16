class Aircraft(object):
    def __init__(self, type):
        #print(type)
        self.type = type

        if type == "F16":
            self.max_ammo = 8
            self.base_dmg = 30
            self.ammo = 0
        elif type == "F35":
            self.max_ammo = 12
            self.base_dmg = 50
            self.ammo = 0

    def damage(self):
        return self.ammo*self.base_dmg
 

    def fight(self):
        dmg_dealt = self.damage()
        self.ammo = 0
        return dmg_dealt
    
    def refill(self, number):
        to_fill = self.max_ammo - self.ammo
        if to_fill > number:
            can_fill = number
        else:
            can_fill = to_fill
        
        self.ammo += can_fill

        return number - can_fill

    def getType(self):
        return self.type

    def getStatus(self):
        #Type F35, Ammo: 10, Base Damage: 50, All Damage: 500"
        return "Type: " + self.getType() + ", Ammo: " + str(self.ammo) +  ", Base Damage: " + str(self.base_dmg) +  ", All Damage: " + str(self.ammo*self.base_dmg)

class Carrier(object):
    def __init__(self, ammoStore, health):
        self.ammoStore = ammoStore
        self.health = health
        self.aircrafts = []

    def addAircraft(self, aircraftType):
        temporaryAircraft = Aircraft(aircraftType)
        self.aircrafts.append(temporaryAircraft)
        #self.aircrafts.append(Aircraft(aircraftType)) # Same as above, but in one line

    def fill(self):
        if self.ammoStore == 0:
            raise Exception("Not enough ammo")

        for craft in self.aircrafts:
            if craft.getType() == "F35":
                self.ammoStore = craft.refill(self.ammoStore)
        
        for craft in self.aircrafts:
            if craft.getType() == "F16":
                self.ammoStore = craft.refill(self.ammoStore)

    def printStatus(self):
        totalDamage = 0
        for craft in self.aircrafts:
            totalDamage += craft.damage()

        print ("Health = " + str(self.health) + " Aircraft count: " + str(len(self.aircrafts)) + " Ammo storage: " + str(self.ammoStore) + " Total damage: "  + str(totalDamage))

        for craft in self.aircrafts:
            print(craft.getStatus())
        

    def fight(self, other):
        for craft in self.aircrafts:
            other.health -= craft.fight()



# aircraft = Aircraft("F16")
# print(aircraft.refill(12))
# print(aircraft.getStatus())
# print(aircraft.fight())
# print(aircraft.refill(5))
# print(aircraft.fight())

try:
    carrier = Carrier(300, 5000)
    carrier.addAircraft("F35")
    carrier.addAircraft("F16")
    carrier.addAircraft("F35")
    carrier.fill()
    carrier.printStatus()

    carrier2 = Carrier(200, 3000)
    carrier2.addAircraft("F35")
    carrier2.addAircraft("F16")
    carrier2.addAircraft("F16")
    carrier2.fill()
    carrier2.printStatus()

    carrier.fight(carrier2)
    carrier.printStatus()
    carrier2.printStatus()
except Exception as value:
    print(value)
    