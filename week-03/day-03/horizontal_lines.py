from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.


def drawer(x, y):
    red_line = canvas.create_line(140, 300, x, y, fill = "red")
    green_line = canvas.create_line(10, 270, x, y, fill = "green")
    blue_line = canvas.create_line(80, 200, x, y, fill = "blue")


drawer(150,150)

root.mainloop()