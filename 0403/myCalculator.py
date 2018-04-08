from tkinter import *
from math import *

def processAndEvaluate (*args):
    answer = '\n'
    instring = str(tbox.get("insert linestart", "insert lineend"))
    instring = instring.replace('>>>><<<<','')
    instring = instring.replace('^','**')
    instring = instring.replace('ln','log')
    instring = instring.replace('×','*')
    instring = instring.replace('I','j')
    instring = instring.lower()
    instring = instring.replace('arc','a')
    try:
        answer += ('=   '+str(eval(instring))+'\n')
    except Exception as Argument:
        answer += (str(Argument)+'\n')
    answer += '>>>><<<<'
    tbox.insert(END,answer)
    return 0


root = Tk()
tbox = Text(root,width=160,height=240)
tbox.pack()
tbox.insert(1.0,'''This my Calculator based on python. You can directly input your expression here.
Use pi or PI for π, exp(1) for e=2.718, and I for the imaginary unit.
>>>><<<<
''')
tbox.bind('<Return>',processAndEvaluate)

root.mainloop()
