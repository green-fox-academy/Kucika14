from tkinter import *
import math
import time
root = Tk()

canvas = Canvas(root, width = 650, height = 650)
canvas.pack()

def draw_hexagon(x, y, size):
    time.sleep(0.6)
    canvas.update()
    height = math.sqrt(3) / 2 * size
    canvas.create_polygon(x, y, x + size / 2, y - height,
                          x + size * 1.5, y - height,
                          x + size * 2, y,
                          x + size * 1.5, y + height,
                          x + size / 2, y + height,
                          fill="", outline="black")

def draw_fractal(x, y, size):
    if size < 15:
        return
    else:
        height = math.sqrt(3) / 2 * size
        draw_hexagon(x, y, size)

        draw_fractal(x+size/4, y-height/2, size / 2)
        draw_fractal(x+size, y, size / 2)
        draw_fractal(x+size/4, y+height/2, size / 2)

draw_fractal(10, 300, 300)

root.mainloop()