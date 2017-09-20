from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
canvas_rect = canvas.create_rectangle(15, 15, 45, 45, fill = "green")
canvas_rect1 = canvas.create_rectangle(145, 145, 155, 155, fill = "blue")
canvas_rect2 = canvas.create_rectangle(240, 240, 280, 280, fill = "red")
canvas_rect3 = canvas.create_rectangle(60, 125, 125, 60, fill = "purple")

# draw four different size and color rectangles.

root.mainloop()