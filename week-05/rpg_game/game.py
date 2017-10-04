from tkinter import *
from view import Display
from map import Map


    
class Game:
    def __init__(self):
        self.my_view = Display()
        self.game_map = Map()
        self.my_view.draw_map(self.game_map.game_map_source)
        self.draw_hero(0,0)
        self.my_view.root.bind("<KeyPress>", self.on_key_press)
        self.my_view.starter()


       
    def draw_hero(self, x, y):
        self.hero = self.my_view.draw_entity(self.my_view.char_down, [x, y])
    
    # def draw_enemy(self, x, y):
    #     self.draw_skeleton1 = self.canvas.create_image(x, y, anchor=NW, image=self.skeleton)
    #     self.draw_skeleton2 = self.canvas.create_image(x, y, anchor=NW, image=self.skeleton)
    #     self.draw_skeleton3 = self.canvas.create_image(x, y, anchor=NW, image=self.skeleton)

    def move(self, dx, dy):
        self.my_view.canvas.move(self.hero, dx*72, dy*72)

              
    def on_key_press(self, e):
        coords = self.my_view.canvas.coords(self.hero)
        if ( e.keysym == 'Up' ):
            self.my_view.canvas.itemconfigure(self.hero, image=self.my_view.char_up)
            if coords[1] > 0 and not self.game_map.get_wall_coords(coords[0], coords[1]-72) == 1:
                self.move(0,-1)
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