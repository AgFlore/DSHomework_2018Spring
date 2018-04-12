from tkinter import *
from tkinter import filedialog
import time

root = Tk()
root.title('TextView')

Button(root,text='Load',command = lambda:loadfile(pathe.get)).grid(row=0,column=0)
pathe = Entry(root,width = 40); pathe.grid(row=0,column=1)
Button(root,text='Save Here',command = lambda:save(pathe.get())).grid(row=0,column=2)
Button(root,text='Save As',command = lambda:save('*')).grid(row=0,column=3)
pad = Text(root)
pad.grid(row=1,column=0,columnspan=4)

def loadfile(path):
    try:
        with open(path,'r') as f:
            pad.delete(1.0,END)
            pad.insert(1.0,f.read())
    except Exception as errinfo:
        pad.delete(1.0,END)
        pad.insert(1.0,str(errinfo))
        time.sleep(0.5)
        newpath = filedialog.askopenfilename(title='Open...',filetypes = [("文件","*.*")])
        loadfile(newpath)
        pathe.delete(0,END)
        pathe.insert(0,newpath)

def save(path):
    if path == '':
        return 0
    try:
        with open(path,'w') as f:
            tmp = pad.get(1.0,END)
            f.write(tmp)
    except Exception as errinfo:
        newpath = filedialog.asksaveasfilename(title='Save...',filetypes = [("文件","*.*")])
        pathe.delete(0,END)
        pathe.insert(0,newpath)

root.mainloop()
