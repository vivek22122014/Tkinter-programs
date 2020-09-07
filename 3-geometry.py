#Geometery

from tkinter import Tk,Label
window=Tk()
window.geometry("400x300")
window.title("GUI")
msg=Label(window,text="Hello Tkinter",
         bg="light blue",
         fg="red",
         font="Times 30")

msg.pack()
