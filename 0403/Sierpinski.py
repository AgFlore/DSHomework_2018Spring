from tkinter import *
root = Tk()
root.title('Sierpinski')
canvas = Canvas(root,width=420,height=366)
canvas.grid(row=1,column=0,columnspan=2)
levels = Entry(root,width=40)
levels.grid(row=0,column=0)
Button(root,text='Draw',command=lambda:draw()).grid(row=0,column=1)

def midpoint(p1,p2):
    return [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
def makeline(p1,p2):
    canvas.create_line(p1[0],p1[1],p2[0],p2[1],tags='line')

def addbrick (levels,p1,p2,p3):
    p4 = midpoint(p2,p3)
    p5 = midpoint(p3,p1)
    p6 = midpoint(p1,p2)
    makeline(p4,p5)
    makeline(p5,p6)
    makeline(p6,p4)
    if levels < 0:
        return 0
    addbrick (levels-1,p1,p5,p6)
    addbrick (levels-1,p2,p4,p6)
    addbrick (levels-1,p3,p4,p5)

def draw ():
    try:
        level = int(levels.get())
    except Exception as fault:
        levels.delete(0,END)
        levels.insert(0,str(fault))
        return 0
    canvas.delete('line')
    p1,p2,p3 = [210,10],[10,356],[410,356]
    makeline(p1,p2)
    makeline(p2,p3)
    makeline(p3,p1)
    addbrick(level,p1,p2,p3)

root.mainloop()
