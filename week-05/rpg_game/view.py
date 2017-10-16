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

    def hero_hud(self, entity):
        rect = self.canvas.create_rectangle(820 - 100, 0, 820 + 100, 50 + 100, fill='green')
        self.canvas.create_text(820,50,fill="white", font="Times 12 bold",

        text="HERO STATS" + "\n" +
        "Defense Point: " + str(entity.dp) + "\n" +
        "Strike Point: " + str(entity.sp) + "\n" +
        "Max HP: " + str(entity.max_hp) + "\n" +
        "Current HP: " + str(entity.current_hp))

    def skeleton_hud(self, enemy):
        rect = self.canvas.create_rectangle(820 - 100, 200 - 100, 820 + 100, 200 + 100, fill='green')
        self.canvas.create_text(820,200, fill="white", font="Times 12 bold",

        text="SKELETON STATS" + "\n" +
        "Defense Point: " + str(enemy.dp) + "\n" +
        "Strike Point: " + str(enemy.sp) + "\n" +
        "Max HP: " + str(enemy.max_hp) + "\n" + 
        "Current HP: " + str(enemy.current_hp))


    def boss_hud(self, enemy):
        rect = self.canvas.create_rectangle(820 - 100, 350 - 100, 820 + 100, 350 + 100, fill='green')
       

        self.canvas.create_text(820,350, fill="white", font="Times 12 bold",
        text="BOSS STATS" + "\n" +
        "Defense Point: " + str(enemy.dp) + "\n" +
        "Strike Point: " + str(enemy.sp) + "\n" +
        "Max HP: " + str(enemy.max_hp) + "\n" + 
        "Current HP: " + str(enemy.current_hp))

    def starter(self):
        self.root.mainloop()


        

        


