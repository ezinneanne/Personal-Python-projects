from tkinter import *
from tkinter import colorchooser

def click():
    #color = colorchooser.askcolor()
    #print(color)
    #colorHex = color[1]
    #print(colorHex)
    #window.config(bg=colorHex)
    window.config(bg=colorchooser.askcolor()[1])#a simpler way to write this
    

window = Tk()

#window.geometry("150*150")
button = Button(text="click me!", command=click)
button.pack()


window.mainloop()

