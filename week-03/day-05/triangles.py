from tkinter import *
import math
import time
root = Tk()

canvas = Canvas(root, width = 650, height = 650)
canvas.pack()

def draw_triangle(x, y, size):
    time.sleep(0.00001)
    canvas.update()
    canvas.create_polygon(x,y, x+size,y, x+size/2,y+size, fill="", outline="black")

def draw_fractal(x, y, size):
    if size < 5:
        return
    else:
        draw_triangle(x, y, size)

        draw_fractal(x, y, size/2)
        draw_fractal(x+size/2, y, size / 2)
        draw_fractal(x+size/4, y+size/2, size / 2)

draw_fractal(10, 10, 600)

root.mainloop()