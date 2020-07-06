from tkinter import *
import random
import time

tk=Tk()
canvas=Canvas(tk, width=600, height=400)
tk.title("ball bounce")
canvas.pack()
ball=canvas.create_oval(10,10,60,60,fill="red")
ball2=canvas.create_oval(310,30,360,80,fill="red")
x=1
y=2
t=1
b=2
while True:
        canvas.move(ball2,-t,b)
        canvas.move(ball, x, y)
        pos1=canvas.coords(ball2)
        pos = canvas.coords(ball)
        if pos1[3] >= 400 or pos1[1] <= 0:
           b = -b
        if pos1[2] >= 600 or pos1[0]<=0:
            t = -t
        if pos[3] >= 400 or pos[1] <= 0:
           y = -y
        if pos[2] >= 600 or pos[0]<=0:
            x = -x
        if pos1[0] == pos[0]+50:
                x=-x
                y=-y
                t=-t
                b=-b
        tk.update()
        time.sleep(0.01)

tk.mainloop()
