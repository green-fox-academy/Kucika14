from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

box_size = 1

def purple_steps_3D(box_size):
    base = 0
    for each in range(30):
        box = canvas.create_rectangle((each + 1) * box_size + base, (each + 1) * box_size + base, (each + 1) * (box_size * 2) + base, (each + 1) * (box_size * 2) + base, fill='purple')
        base += each * box_size

purple_steps_3D(box_size)
root.mainloop()