from tkinter import *


window = Tk()

canvas = Canvas(window)
#canvas.create_line(0,0,1000,1000,fill="blue",width=5)
#canvas.create_line(0,1000,1000,0,fill="red",width=5)
#canvas.create_rectangle(50,50,250,250,fill="purple")
#canvas.create_polygon(250,0,500,500,0,500,fill="green",outline="blue",width=5)
#canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,extent=180)

canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)

canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)

canvas.create_oval(190,190,310,310,fill="white",width=10)


canvas.pack()


window.mainloop()
