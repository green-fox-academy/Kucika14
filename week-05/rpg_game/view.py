from tkinter import *
from map import Map
from random import randint
from entity import Hero, Skeleton, Boss



class Display:
    def __init__(self):
        self.size = 720
        self.root = Tk()
        self.root.configure(background ='black')
        self.hud = 200
        self.canvas = Canvas(self.root, width=self.size+self.hud, height=self.size,bg="green",bd=0)
        self.floor = PhotoImage(file="floor.png")
        self.wall = PhotoImage(file="wall.png")
        self.char_down = PhotoImage(file="hero-down.png")
        self.char_up = PhotoImage(file="hero-up.png")
        self.char_right = PhotoImage(file="hero-right.png")
        self.char_left = PhotoImage(file="hero-left.png")
        self.skeleton = PhotoImage(file="skeleton.png")
        self.boss = PhotoImage(file="boss.png")
        self.hero = Hero()
        self.warlock = Boss()
        self.bones = Skeleton()
        self.hero_hud()
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

    def hero_hud(self):
        self.canvas.create_text(820,50,fill="white", font="Times 12 bold",
        text="HERO STATS" + "\n" +
        "Defense Point: " + str(self.hero.dp) + "\n" +
        "Strike Point: " + str(self.hero.sp) + "\n" +
        "Max HP: " + str(self.hero.max_hp))

    def skeleton_hud(self, enemy):
        self.canvas.create_text(820,200, fill="white", font="Times 12 bold",
        text="SKELETON STATS" + "\n" +
        "Defense Point: " + str(self.bones.dp) + "\n" +
        "Strike Point: " + str(self.bones.sp) + "\n" +
        "Max HP: " + str(self.bones.max_hp))

    def boss_hud(self, enemy):
        self.canvas.create_text(820,350, fill="white", font="Times 12 bold",
        text="BOSS STATS" + "\n" +
        "Defense Point: " + str(self.warlock.dp) + "\n" +
        "Strike Point: " + str(self.warlock.sp) + "\n" +
        "Max HP: " + str(self.warlock.max_hp))

    def starter(self):
        self.root.mainloop()


        

        


