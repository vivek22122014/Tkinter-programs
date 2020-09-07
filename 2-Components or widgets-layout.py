#Components or widgets
#Layout

class component:
    def pack(self):
        #Fits component to window
        return
    def grid(self,row,col):
        #arrange in row-columnformat
        return 
    def place(self,x,y):
        #place@ specified (x,y)co-ordinate
        return
from tkinter import Tk, Label
window=Tk()
msg=Label(window,text="Hello Tkinter")
msg.pack()
