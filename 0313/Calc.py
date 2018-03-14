operator = dict((('+',(lambda a,b : a+b)),('-',(lambda a,b : a-b)),('*',(lambda a,b : a*b)),('/', (lambda a,b : a/b))))
inexp = input('输入\n')
a = o = b = ""
for ch in list(operator.keys()):
    a,o,b = inexp.partition(ch)
    if o != ch:
        continue
    break
if o == '':
    print('没有运算符！')
    exit()
an = int(a.strip())
bn = int(b.strip())
print (operator.get(o)(an,bn))
