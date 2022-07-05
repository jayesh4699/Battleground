# Firstly import Tkinter Module
from tkinter import *
from tkinter.ttk import *
import tkinter as tk

def dp():
    program.config(bg="yellow")

# Then create a program Tkinter window
program = Tk()
# Photoimage class is created
# And Image should be in the same folder where there is script saved
p1 = PhotoImage(file = 'C:/Users/jayes/OneDrive/Desktop/images.png')
# Icon set for program window
program.iconphoto(False, p1)
# Button creation
b = Button(program, text = 'Press Me!',command=dp)
b.pack(side = TOP)
program.title('iconphoto() method')
mainloop()
