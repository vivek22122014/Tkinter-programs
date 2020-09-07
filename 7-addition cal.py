from tkinter import *
def add():
    s1=e1.get()
    s2=e2.get()
    if s1=='' or s2=='':
        err.set("Field cannot be empty")
    else:
        try:
            x=int(s1)
            y=int(s2)
            z=x+y
            res.set(str(z))
        except ValueError:
            err.set("Invalid Input...")
    return
window=Tk()
window.title("Calculator")
res=StringVar()
err=StringVar()
l1=Label(window,text="Enter Input:",font="Times 20")
e1=Entry(window,font="Times 20")

l2=Label(window,text="+",font="Times 20")
e2=Entry(window,font="Times 20")

l3=Label(window,text="=",font="Times 20")
e3=Entry(window,font="Times 20",textvariable=res)

b1=Button(window,text="add",command=add,font="Times 20")
l4=Label(window,textvariable=err,font='Times 20',fg='red')

l1.grid(row=0,column=0)
e1.grid(row=0,column=1)

l2.grid(row=0,column=2)
e2.grid(row=0,column=3)

l3.grid(row=0,column=4)
e3.grid(row=0,column=5)

b1.grid(row=0,column=6)
l4.grid(row=1,column=3)

