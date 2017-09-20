from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

canvas_width = 300
canvas_height = 300

def star():
    for each in range(canvas_width//20):
        line = canvas.create_line(x, y+each*20, x + each * 20, canvas_height, fill = "green")





star()
root.mainloop()