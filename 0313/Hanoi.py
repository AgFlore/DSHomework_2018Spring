def Hanoi(n,x,y,z):
    if n == 1:
        print (x,'>>',z)
    else:
        Hanoi(n-1,x,y,z)
        print (x,'>>',z)
        Hanoi(n-1,y,z,x)
    return 0
Hanoi(3,'A','B','C')
print('\n')
Hanoi(4,'A',"B",'C')
