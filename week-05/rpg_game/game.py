from tkinter import *
from view import Display
from map import Map
from random import randint


    
class Game:
    def __init__(self):
        self.my_view = Display()
        self.game_map = Map()
        self.my_view.draw_map(self.game_map.game_map_source)
        self.chars_on_screen = []
        self.draw_hero(0,0)
        self.draw_enemy()
        self.my_view.root.bind("<KeyPress>", self.on_key_press)
        self.my_view.starter()

       
    def draw_hero(self, x, y):
        self.hero = self.my_view.draw_entity(self.my_view.char_down, [x, y])
        self.chars_on_screen.append(self.hero)

    
    def draw_enemy(self):
        self.skeleton1 = self.my_view.draw_entity(self.my_view.skeleton, self.random_spawn())
        self.chars_on_screen.append(self.skeleton1)
        self.skeleton2 = self.my_view.draw_entity(self.my_view.skeleton, self.random_spawn())
        self.chars_on_screen.append(self.skeleton2)
        self.skeleton3 = self.my_view.draw_entity(self.my_view.skeleton, self.random_spawn())
        self.chars_on_screen.append(self.skeleton3)
        self.boss = self.my_view.draw_entity(self.my_view.boss, self.random_spawn())
    

    def random_spawn(self):
        coords = [0, 0]
        while self.is_occupied(coords[0],coords[1]) or self.game_map.get_wall_coords(coords[0]*72,coords[1]*72) == 1:
            coords[0] = randint(0,9)
            coords[1] = randint(0,8)
        return coords
        
    def is_occupied(self, x, y):
        for image in self.chars_on_screen:
            coords = self.my_view.canvas.coords(image)
            its_occupied = coords[0] == x and coords[1] == y
            if its_occupied:
                break
        return its_occupied
        
    def battle(self, x, y):
        if self.is_occupied(x,y):
            self.my_view.game_hud()

    def move(self, dx, dy):
        self.my_view.canvas.move(self.hero, dx*72, dy*72)

              
    def on_key_press(self, e):
        coords = self.my_view.canvas.coords(self.hero)
        if ( e.keysym == 'Up' ):
            self.my_view.canvas.itemconfigure(self.hero, image=self.my_view.char_up)
            if coords[1] > 0 and not self.game_map.get_wall_coords(coords[0], coords[1]-72) == 1:
                self.move(0,-1)
                self.battle(coords[0], coords[1])
        elif( e.keysym == 'Down' ):
            self.my_view.canvas.itemconfigure(self.hero, image=self.my_view.char_down)
            if coords[1] < 648 and not self.game_map.get_wall_coords(coords[0], coords[1]+72) == 1:
                self.move(0,1)
        elif( e.keysym == 'Right'):
            self.my_view.canvas.itemconfigure(self.hero, image=self.my_view.char_right)
            if coords[0] < 648 and not self.game_map.get_wall_coords(coords[0]+72, coords[1]) == 1:
                self.move(1,0)
        elif( e.keysym == 'Left'):
            self.my_view.canvas.itemconfigure(self.hero, image=self.my_view.char_left)
            if coords[0] > 0 and not self.game_map.get_wall_coords(coords[0]-72, coords[1]) == 1:
                self.move(-1,0)

game = Game()