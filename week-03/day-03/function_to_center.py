from tkinter import *
import random
root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.


color = ["green","blue", "yellow", "orange", "purple", "pink", "grey", "brown", "red"]
line_x = 0
line_y = 0
def sea_urchin(x,y):
    center = 150
    for each in range(15):
        line = canvas.create_line(x+each*20, y, center, center, fill = color[random.randint(0, len(color)-1)])
        line = canvas.create_line(x, y+each*20, center, center, fill = color[random.randint(0, len(color)-1)])
        line = canvas.create_line(300, y+each*20, center, center, fill = color[random.randint(0, len(color)-1)])
        line = canvas.create_line(x+each*20, 300, center, center, fill = color[random.randint(0, len(color)-1)])
        
        # x += 20
        # y += 20        
sea_urchin(line_x, line_y)

root.mainloop()