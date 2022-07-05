from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title('GUI_Layout')
GUI.geometry('500x300')

L1 = Label(GUI,text='hello 1 - pack')
L1.pack()

L2 = Label(GUI,text='hello 2 - place')
L2.place(x=100,y=200)

F1 = ttk.LabelFrame(GUI,text='grid color')
F1.place(x=150,y=200)

L3 = Label(F1,text='hello 3 - grid',bg='red')
L3.grid(row=0,column=0)

L4 = Label(F1,text='hello 4 - grid',bg='green')
L4.grid(row=0,column=1)

L5 = Label(F1,text='hello 5 - grid',bg='orange')
L5.grid(row=1,column=1)

L5 = Label(F1,text='hello 6 - grid',bg='blue',fg='white')
L5.grid(row=2,column=2)

GUI.mainloop()
