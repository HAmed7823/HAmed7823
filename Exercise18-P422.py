from tkinter import Tk, Canvas
from tkinter.ttk import Button,Frame


def press_black():
    color = 'black'
    if color=='black':
        canvas.itemconfigure(yellow_lamp,fill='black')
def press_yellow():
    color = 'yellow'
    if color=='yellow':
        canvas.itemconfigure(yellow_lamp,fill='yellow')

root=Tk()
root.title('traffic light')
frame = Frame(root)
frame.pack()
canvas = Canvas(frame , width=80,height=80)
yellow_lamp = canvas.create_oval(10,30,60,80,fill='black')
button = Button(frame,text='On',command=press_yellow)
button2 = Button(frame,text='OFF',command=press_black)
button.grid(row=0,column=0)
button2.grid(row=1,column=0)
canvas.grid(row=0,column=1)
root.mainloop()
