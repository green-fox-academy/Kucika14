from tkinter import *

class Map:
    def __init__(self):
        self.size = 720
        self.root = Tk()
        self.root.configure(background ='black')
        self.hud = 120
        self.canvas = Canvas(self.root, width=self.size+self.hud, height=self.size,bg="yellow",bd=0)
        self.floor = PhotoImage(file="floor.png")
        self.draw_map()
        self.canvas.pack()

    def draw_map(self):
        size = 72
        for row in range(10):
            for column in range(10):
                x = column*size
                y = row*size
                self.canvas.create_image(x+36, y+36, image=self.floor)
    def display(self):
        self.draw_map()
        self.root.mainloop()
new_map = Map()
new_map.display()
