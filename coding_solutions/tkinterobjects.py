from tkinter import*
import random
tk=Tk()
canvas=Canvas(tk,width=500,height=400)
tk.title("drawing")
canvas.pack()
canvas.create_line(0,0,76,89)
canvas.create_oval(230,230,50,50,fill="blue")
canvas.create_rectangle(300,300,400,400,fill='black')
canvas.create_polygon(200,200,250,150,300,200,300,200,250,fill="brown")
