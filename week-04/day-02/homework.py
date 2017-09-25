class Person(object):

    def __init__(self, name='Jane Doe', age=30, gender='female'):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print('Hi, I\'m ' + self.name + ' a ' + str(self.age) + ' year old ' + self.gender + '.')
        return self

    def get_goal(self):
        print("My goal is: Live for the moment!")

class Student(object):

    def __init__(self, name='Jane Doe', age=30, gender='female',\
    previous_organization='The school of life', skipped_days=0):
        self.name = name
        self.age = age
        self.gender = gender
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print("Be a junior software developer.")
        return self

    def introduce(self):
        print('Hi, I\'m ' + self.name + ' a ' + str(self.age) + ' year old ' + \
        self.gender + ' from '+ self.previous_organization + ' who skipped ' + \
        str(self.skipped_days) + ' days from the course already.')











student = Student()
student.get_goal().introduce()
person = Person()
person.name = 'Joci'
person.introduce().get_goal()
    