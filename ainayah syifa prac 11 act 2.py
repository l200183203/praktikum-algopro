#Practic 11. Activity 2. Make Simple Calculator. by@Ainayah Syifa Hendri
from Tkinter import Tk, Label, Entry, Button, StringVar

my_app = Tk(className= "Simple calculator")

L1 = Label(my_app, text= "Number 1")
L1.grid(row=0, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable= str1)
E1.grid(row=0, column=1, columnspan=3)
L2 = Label(my_app, text= "Number 2")
str2 = StringVar()
L2.grid(row=1, column=0)
E2 = Entry(my_app, textvariable= str2)
E2.grid(row=1, column=1, columnspan=3)

def plus():
    p = float(str1.get())
    q = float(str2.get())
    r = p+q
    L.config(text=r)

def minus():
    p = float(str1.get())
    q = float(str2.get())
    r = p-q
    L.config(text=r)

def times():
    p = float(str1.get())
    q = float(str2.get())
    r = p*q
    L.config(text=r)

def divide():
    p = float(str1.get())
    q = float(str2.get())
    r = p/q
    L.config(text=r)

B1 = Button (my_app, text= "+", command = plus)
B1.grid(row=2, column=0)
B2 = Button (my_app, text= "-", command = minus)
B2.grid(row=2, column=1)
B3 = Button (my_app, text= "x", command = times)
B3.grid(row=2, column=2)
B4 = Button (my_app, text= ":", command = divide)
B4.grid(row=2, column=3)

L3 = Label (my_app, text= "Results")
L3.grid (row=3, column=1)
L = Label(my_app, text= "0")
L.grid(row=3, column=2)

my_app.mainloop()
