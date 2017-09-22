from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

size = 300/8



def checkerboard(size):
    for i in range(8):
        for j in range(8):
            x = j*size
            y = i*size
            if (i+j) %2==0:
                canvas.create_rectangle(x, y ,x+size, y+size,fill="black")



checkerboard(size)
root.mainloop()