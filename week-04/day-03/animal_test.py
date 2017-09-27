from animal import Animal
import unittest
my_animal = Animal()
class AnimalTest(unittest.TestCase):

    def test_eat(self):
        my_animal.eat()
        self.assertEqual(my_animal.hunger, 49)

    def test_drink(self):
        my_animal.drink()
        self.assertEqual(my_animal.thirst, 49)

    def test_drink(self):
        my_animal.drink()
        my_animal.drink()
        self.assertEqual(my_animal.thirst, 48)

    def test_play(self):
        my_animal.play()
        self.assertEqual(my_animal.thirst, 49)
        self.assertEqual(my_animal.hunger, 50)

if __name__ == '__main__':
    unittest.main()