class Counter(object):
    def __init__(self, number=0):
        self.number = number
        self.init_number = number

    def add(self, num=1):
        self.number += num

    def get(self):
        return self.number
    
    def reset(self):
        self.number = self.init_number

counter = Counter()
counter.add()
counter.reset()
print(counter.get())