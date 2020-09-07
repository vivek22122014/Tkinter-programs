#StringVar

from tkinter import *
window=Tk()
msg=StringVar()
l=Label(window,textvariable=msg,font="Times 50")
l.pack()
name=input("Enter your name:")
msg.set(name)
