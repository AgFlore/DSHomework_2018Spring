import numbers
from tkinter import *
root = Tk()
root.title('Calculator')
res = StringVar()

e1 = Entry(root,width=10);
e1.grid(row=0,column=0)

Label(root,text='+').grid(row=0,column=1)

e2 = Entry(root,width=10);
e2.grid(row=0,column=2)

Label(root,text = '=').grid(row=0,column=3)

e3 = Entry(root,width=20,textvariable = res)
e3.grid(row=0,column=4)

def calc ():
    try:
        res.set(float(e1.get())+float(e2.get()))
    except ValueError:
        res.set('NAN')

Button(root,text='GO!',command=calc).grid(row=1,column=3)

root.mainloop()
