from tkinter import *
import math
import time
root = Tk()

canvas = Canvas(root, width = 650, height = 650)
canvas.pack()

def draw_rectangle(x, y, size):
    time.sleep(0.1)
    canvas.update()
    canvas.create_rectangle(x+size/3,y+size/3, x+size, y+size, fill="", outline="black")

def draw_fractal(x, y, size):
    if size < 5:
        return
    else:
        draw_rectangle(x, y, size)

        draw_fractal(x-size/2, y-size/2, size/2)
        # draw_fractal(x+size/2, y)
        # draw_fractal(x+size/4, y+size/2)

draw_fractal(0, 0, 600)

root.mainloop()