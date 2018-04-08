from datetime import datetime
from tkinter import *
root = Tk()
thetime = Label(root, fg='blue', font=('times',70))
root.title('Clock')

def tick():
    thetime.config(text=str(datetime.now()).split()[1])
    thetime.after(10,tick)

thetime.pack()
tick()
root.mainloop()
