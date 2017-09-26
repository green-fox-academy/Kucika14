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

class Student(Person):

    def __init__(self, name='Jane Doe', age=30, gender='female',\
    previous_organization='The school of life', skipped_days=0):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print("Be a junior software developer.")
        return self

    def introduce(self):
        print('Hi, I\'m ' + self.name + ' a ' + str(self.age) + ' year old ' + \
        self.gender + ' from '+ self.previous_organization + ' who skipped ' + \
        str(self.skipped_days) + ' days from the course already.')


class Mentor(Person):

    def __init__(self, name='Jane Doe', age=30, gender='female', level='intermediate'):
        super().__init__(name, age, gender)
        self.level = level


    def introduce(self):
        print('Hi, I\'m ' + self.name + ' a ' + str(self.age) + ' year old ' + self.gender + " " + self.level + ' mentor.')
        return self

    def get_goal(self):
        print("Educate brilliant junior software developers.")


class Sponsor(Person):
    def __init__(self, name='Jane Doe', age=30, gender='female',\
    company='Google', hired_students=0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def hire(self):
        self.hired_students += 1

    def introduce(self):
        print('Hi, I\'m ' + self.name + ' a ' + str(self.age) + ' year old ' + \
        self.gender + ' who represents ' + self.company +' and hired ' + \
        str(self.hired_students) +' students so far.')
        return self

    def get_goal(self):
        print("Hire brilliant junior software developers.")


class PallidaClass(object):
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.mentors = []


    def add_student(self, student):
        studnets = []
        self.students.append(Student)

    def add_mentor(self, mentor):
        mentors = []
        self.mentors.append(Mentor)
    
    def info(self):
        print('Pallida ' + self.class_name+' class has ' + \
        str(len(self.students)) +' students and ' + \
        str(len(self.mentors)) +  ' mentors.')

bela = Student()
sponsor = PallidaClass('Rabbit')
sponsor.add_student(bela)
sponsor.info()
