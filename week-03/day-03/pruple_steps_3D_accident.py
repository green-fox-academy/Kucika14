from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

size_x = 1
size_y = 1
def purple_steps_3D(x, y):
    base = 0
    for i in range(40):
        rect = canvas.create_rectangle((i+1)*x+base, (i+1)*x+base, (i+1)*(y*2)+base, (i+1)*(y*2)+base, fill = "purple")
        # x += 15
        # y += 15
        base += i * base

purple_steps_3D(size_x,size_y)
root.mainloop()