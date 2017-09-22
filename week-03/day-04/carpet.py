from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

width = 600
height = 600

x = width/3
y = 0

def carpet(x,y):
    for i,j in ([0,0],[1,1],[0,2],[-1,1]):
        rect = canvas.create_rectangle(x+x*i, y+j*x, 2*x+i*x, x+y+j*x, fill = "yellow")
    





carpet(x,y)
root.mainloop()