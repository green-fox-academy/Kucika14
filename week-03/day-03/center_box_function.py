from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.


def draw_rect(size):
    red_line = canvas.create_rectangle(size, size, 200, 200, fill = "red")
    green_line = canvas.create_rectangle(size, size, 200, 100, fill = "green")
    blue_line = canvas.create_rectangle(size, size, 100, 100, fill = "blue")


draw_rect(150)
root.mainloop()