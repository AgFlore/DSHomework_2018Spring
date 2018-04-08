from tkinter import *
root = Tk()
root.title('选项目')
sports = ['足球','篮球','游泳','田径']
v = []
l1 = Label(root,text='请选择项目：')
l2 = Label(root)
l1.pack()
for sport in sports:
    v.append(IntVar())
    b = Checkbutton(root,text=sport,variable=v[-1])
    b.pack(anchor='w')

def reply():
    rep = '您选择了'
    for i in range(len(v)):
        if v[i].get():
            rep += sports[i]
    l2.config(text=rep)
    return 0

thebutton = Button(root,text='好',command=reply)
thebutton.pack()
l2.pack()

root.mainloop()
