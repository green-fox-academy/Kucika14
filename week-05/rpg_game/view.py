from tkinter import *
from map import Map
from random import randint
# from entity import Hero



class Display:
    def __init__(self):
        self.size = 720
        self.root = Tk()
        self.root.configure(background ='black')
        self.hud = 120
        self.canvas = Canvas(self.root, width=self.size+self.hud, height=self.size,bg="yellow",bd=0)
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
        self.char_down = PhotoImage(file="hero-down.png")
        self.char_up = PhotoImage(file="hero-up.png")
        self.char_right = PhotoImage(file="hero-right.png")
        self.char_left = PhotoImage(file="hero-left.png")
        self.skeleton = PhotoImage(file="skeleton.png")
        self.game_map = Map()
        # self.hero_draw = Hero()
        self.draw_map()
        self.canvas.pack()
        self.root.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()

    def draw_map(self):
        size = 72
        for row in range(10):
            for column in range(10):
                x = column*size
                y = row*size
                self.canvas.create_image(x, y, anchor=NW, image=self.floor)
                if self.game_map.game_map_source[row][column]==1:
                    self.canvas.create_image(x, y, anchor=NW, image=self.wall)

    def draw_hero(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image=self.char_down)
    
    def draw_skeletons(self, x, y):
        size = 72
        skeleton = 0
        for row in range(len(self.game_map.game_map_source)):
            for column in range(len(self.game_map.game_map_source)):
                if skeleton <=4:
                    x = column*size
                    y = row*size
                    if self.game_map.game_map_source[row][column]!=1:
                        num = randint(1,10)
                        if num == 1:
                            self.draw_skeleton = self.canvas.create_image(x, y, anchor=NW, image=self.skeleton)
                            skeleton += 1

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx*72, dy*72)
                
    def on_key_press(self, e):
        coords = self.canvas.coords(self.hero)
        if ( e.keysym == 'Up' ):
            self.canvas.itemconfigure(self.hero, image=self.char_up)
            if coords[1] > 0 and not self.get_wall_coords(coords[0], coords[1]-72) == 1:
                self.move(0,-1)
        elif( e.keysym == 'Down' ):
            self.canvas.itemconfigure(self.hero, image=self.char_down)
            if coords[1] < 648 and not self.get_wall_coords(coords[0], coords[1]+72) == 1:
                self.move(0,1)
        elif( e.keysym == 'Right'):
            self.canvas.itemconfigure(self.hero, image=self.char_right)
            if coords[0] < 648 and not self.get_wall_coords(coords[0]+72, coords[1]) == 1:
                self.move(1,0)
        elif( e.keysym == 'Left'):
            self.canvas.itemconfigure(self.hero, image=self.char_left)
            if coords[0] > 0 and not self.get_wall_coords(coords[0]-72, coords[1]) == 1:
                self.move(-1,0)
    
    def get_wall_coords(self,x ,y):
        x = int(x//72)
        y = int(y//72)
        return self.game_map.game_map_source[y][x]
           
            
    def starter(self):
        self.root.mainloop()


        

        


