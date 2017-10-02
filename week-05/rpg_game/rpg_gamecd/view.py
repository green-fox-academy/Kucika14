from tkinter import *

class Map:
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
                self.canvas.create_image(x+36, y+36, image=self.floor)
                if game_map_source[row][column]==1:
                    self.canvas.create_image(x+36, y+36, image=self.wall)
                
    def on_key_press(self, e):
        coords = self.canvas.coords(self.hero)
        self.canvas.delete(self.hero)
        if ( e.keysym == 'Up' ):
            self.hero = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.char_up)
            if coords[1] > 0:
                self.move(0,-1)
        elif( e.keysym == 'Down' ):
            self.hero = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.char_down)
            if coords[1] < 648:
                self.move(0,1)
        elif( e.keysym == 'Right'):
            self.hero = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.char_right)
            if coords[0] < 648:
                self.move(1,0)
        elif( e.keysym == 'Left'):
            self.hero = self.canvas.create_image(coords[0], coords[1], anchor=NW, image=self.char_left)
            if coords[0] > 0:
                self.move(-1,0)
    
           
            
    def display(self):
        self.root.mainloop()

    def base_shape(self, x, y):
        self.hero = self.canvas.create_image(x, y, anchor=NW, image=self.char_down)

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx*72, dy*72)



# Tell the canvas that we prepared a function that can deal with the key press events

# Select the canvas to be in focused so it actually recieves the key hittings

game_map_source = [
    [0,0,0,1,0,1,0,0,0,0],
    [0,0,0,1,0,1,0,1,1,0],
    [0,1,1,1,0,1,0,1,1,0],
    [0,0,0,0,0,1,0,0,0,0],
    [1,1,1,1,0,1,1,1,1,0],
    [0,1,0,1,0,0,0,0,1,0],
    [0,1,0,1,0,1,1,0,1,0],
    [0,0,0,0,0,1,1,0,1,0],
    [0,1,1,1,0,0,0,0,1,0],
    [0,0,0,1,0,1,1,0,0,0]
]