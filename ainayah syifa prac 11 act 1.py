## Practice 1. Showing self data. by@Ainayah Syifa Hendri
from Tkinter import Tk, Label, Entry, Button, StringVar
from tkMessageBox import showinfo

my_app = Tk(className = 'Personal Data')

A1 = Label(my_app, text = 'Personal data', font = ('Arial', 24))
A1.grid(row = 0, column = 0)

L1 = Label(my_app, text = 'Name')
L1.grid(row = 1, column = 0)
str1 = StringVar(value='Ainayah Syifa Hendri')
E1 = Entry(my_app, textvariable=str1)
E1.grid(row = 1, column = 1)

L2 = Label(my_app, text = 'NIM')
L2.grid(row = 2, column = 0)
str2 = StringVar(value='L200183203')
E2 = Entry(my_app, textvariable=str2)
E2.grid(row = 2, column = 1)

S1 = Label(my_app, text = 'Favourite book')
S1.grid(row = 3, column = 0)
str3 = StringVar(value='Sherlock Holmes')
Y1 = Entry(my_app, textvariable=str3)
Y1.grid(row = 3, column = 1)

S2 = Label(my_app, text = 'Idol among friends')
S2.grid(row = 4, column = 0)
str4 = StringVar(value='Khalid bin Walid')
Y2 = Entry(my_app, textvariable=str4)
Y2.grid(row = 4, column = 1)

I1 = Label(my_app, text = 'Motto')
I1.grid(row = 5, column = 0)
str5 = StringVar(value='I know i can')
F1 = Entry(my_app, textvariable=str5)
F1.grid(row = 5, column = 1)

def close():
    my_app.destroy()

B1 = Button(my_app.quit(), text = 'Close', command = close)
B1.grid(row = 6, column = 1)


my_app.mainloop()
