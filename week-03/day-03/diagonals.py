from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
green_line = canvas.create_line(0, 0, 300, 300, fill = "green")
green_line2 = canvas.create_line(0, 300, 300, 0, fill = "green")
canvas.pack()

# draw the canvas' diagonals in green.

root.mainloop()