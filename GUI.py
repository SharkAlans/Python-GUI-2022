print('Welcome to this program!')

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('GUI')
GUI.geometry('500x300')

def Show():
    messagebox.showinfo('Show Box','')

B1 = ttk.Button(GUI,text='Click Here',command=Show)
B1.pack(ipadx=30,ipady=20,pady=50)

'''
B1 = ttk.Button(GUI,text='Click Here',command=Show)
B1.pack(ipadx=30,ipady=20)

B1 = ttk.Button(GUI,text='Click Here',command=Show)
B1.pack(ipadx=30)

B1 = ttk.Button(GUI,text='Click Here',command=Show)
B1.pack()
'''

GUI.mainloop()
