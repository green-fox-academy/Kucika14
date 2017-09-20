from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def drawer(x, y):
    red_line = canvas.create_rectangle(x, y, 150, 150, fill = "red")
    green_line = canvas.create_rectangle(x, y, 150, 50, fill = "green")
    blue_line = canvas.create_rectangle(x, y, 50, 50, fill = "blue")


drawer(100,100)

root.mainloop()
