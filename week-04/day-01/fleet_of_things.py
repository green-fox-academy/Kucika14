from thing import Thing

class Fleet(object):
    def __init__(self):
        self.things = []

    def add(self, thing):
        self.things.append(thing)

    def __str__(self):
        result = ""
        for i in range(0, len(self.things)):
            result += str(i+1) + ". " + self.things[i].__str__() + "\n"
        return result



thing1 = Thing('Get milk')
thing2 = Thing('Remove the obstacles')
thing3 = Thing('Stand up')
thing4 = Thing('Eat lunch')
fleet = Fleet()
fleet.add(thing1)
fleet.add(thing2)
fleet.add(thing3)
fleet.add(thing4)
thing3.complete()
thing4.complete()
print(fleet)
