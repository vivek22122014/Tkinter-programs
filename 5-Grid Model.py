#Grid Model

from tkinter import Tk, Button, Label, Entry
def display():
    name=e1.get()
    loc=e2.get()
    print(name+"Living in:"+loc)
    return
window=Tk()
l1=Label(window,text="Name:",font="Times 35")
l2=Label(window,text="Loc:",font="Times 35")

e1=Entry(window,font="Times 35")
e2=Entry(window, font="Times 35")

b1=Button(window,text="Display",font="Times 25", command= display)
b2=Button(window,text="Exit",font="Times 25", command= quit)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)


l2.grid(row=1,column=0)
e2.grid(row=1,column=1)


b1.grid(row=2,column=0)
b2.grid(row=2,column=1)







    
