from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
red_line = canvas.create_line(10, 10, 290, 10, fill = "red")
green_line = canvas.create_line(10, 10, 10, 290, fill = "green")
blue_line = canvas.create_line(10, 290, 290, 290, fill = "blue")
black_line = canvas.create_line(290, 10, 290, 290, fill = "black")

canvas.pack()

# draw a box that has different colored lines on each edge.

root.mainloop()