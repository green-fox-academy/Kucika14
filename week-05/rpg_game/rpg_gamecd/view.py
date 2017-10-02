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
        self.char = PhotoImage(file="hero-down.png")
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
        if ( e.keysym == 'Up' ):
            self.move(0,-10)
        elif( e.keysym == 'Down' ):
            self.move(0,10)
        elif( e.keysym == 'Right'):
            self.move(10,0)
        elif( e.keysym == 'Left'):
            self.move(-10,0)
            
    def display(self):
        self.root.mainloop()

    def base_shape(self, x, y):
        self.hero = self.canvas.create_image(x+36, y+36, image=self.char)

    def move(self, dx, dy):
        self.canvas.move(self.hero, dx, dy )



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