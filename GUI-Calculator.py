from tkinter import *
from tkinter import ttk, messagebox
import csv


def writetocsv():
    with open('data.csv','a',newline='',encodeing='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


GUI = Tk()
GUI.title('GUI-Calculator')
GUI.geometry('500x300')

L1 = Label(GUI,text='Tuna Fish Weight <Kilograms>',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar()

E1 = ttk.Entry(GUI, textvariable= v_kilo, width=10,justify='right',font=('impact',30))
E1.pack(pady=20)

def Calc(event=None):
    print('Calculating...Please Wait')
    kilo = float(v_kilo.get())
    print(kilo * 5)
    calc_result = kilo * 5
    data = ['Tuna', '{:,.2f}'.format(calc_result)]
    writetocsv(data)
    messagebox.showinfo('Price','Total Price: $ {:,.2f} ($5.00 per kilogram)'.format(calc_result))                

B1 = ttk.Button(GUI,text='Calculate price',command=Calc)
B1.pack(ipadx=40,ipady=30)

E1.bind('<Return>',Calc)

# B2 = ttk.Button(GUI)
# B2.pack()

GUI.mainloop()
