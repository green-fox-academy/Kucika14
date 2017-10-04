from tkinter import *
from map import Map
from random import randint



class Display:
    def __init__(self):
        self.size = 720
        self.root = Tk()
        self.root.configure(background ='black')
        self.hud = 120
        self.canvas = Canvas(self.root, width=self.size+self.hud, height=self.size,bg="grey",bd=0)
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
        self.char_down = PhotoImage(file="hero-down.png")
        self.char_up = PhotoImage(file="hero-up.png")
        self.char_right = PhotoImage(file="hero-right.png")
        self.char_left = PhotoImage(file="hero-left.png")
        self.skeleton = PhotoImage(file="skeleton.png")
        self.boss = PhotoImage(file="boss.png")
        self.canvas.pack()
        self.canvas.focus_set()

    def draw_map(self, game_map):
        size = 72
        for row in range(10):
            for column in range(10):
                x = column*size
                y = row*size
                self.canvas.create_image(x, y, anchor=NW, image=self.floor)
                if game_map[row][column]==1:
                    self.canvas.create_image(x, y, anchor=NW, image=self.wall)

    def draw_entity(self, image, coords):
        self.entity = self.canvas.create_image(coords[0]*72, coords[1]*72, anchor=NW, image=image)
        return self.entity
            
    def starter(self):
        self.root.mainloop()


        

        


