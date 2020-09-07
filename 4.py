from tkinter import Tk, Button
def display():
    print("Button cliked...")
    return
window=Tk()
window.geometry("400x300")
window.title("GUI")

b=Button(window, text="click me",
         font="Times 25",
         command=display)
b.place(x=100,y=100)
