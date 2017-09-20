from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.



def drawer(x, y):
    red_line = canvas.create_line(x, y, 150, 300, fill = "red")
    green_line = canvas.create_line(x, y, 300, 150, fill = "green")
    blue_line = canvas.create_line(x, y, 290, 290, fill = "blue")


drawer(150,150)

root.mainloop()