from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

color = ["green","blue", "yellow", "orange", "purple", "pink", "grey", "brown", "red"]
size = 300

def rainbow_rect(size,color):
    origo = 150-size/2
    for i in range(len(color)):
        rect = canvas.create_rectangle(origo + (i - 1) * 10, origo + (i - 1) * 10, origo+size - (i - 1) * 10, origo+size - (i - 1) * 10, fill = color[random.randint(0, len(color)-1)])


rainbow_rect(size, color)

root.mainloop()