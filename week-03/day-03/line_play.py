from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas_width = 300
canvas_height = 300

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]


line_x = 0
line_y = 0
def fract(x,y):
    for each in range(canvas_width//20):
        line = canvas.create_line(x, y+each*20, x + each * 20, canvas_height, fill = "green")
        line = canvas.create_line(x + each * 20, y, canvas_height, y+each*20, fill = "green")



fract(line_x, line_y)

root.mainloop()