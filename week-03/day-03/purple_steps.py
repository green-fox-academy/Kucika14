from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

size_x = 15
size_y = 30
def purple_steps(x, y):
    for i in range(12):
        rect = canvas.create_rectangle(x, x, y, y, fill = "purple")
        x += 15
        y += 15


purple_steps(size_x, size_y)
root.mainloop()