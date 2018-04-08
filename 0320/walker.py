import os;
def mywalker(dirr):
    if os.path.isdir(dirr):
        for dongxi in os.listdir(dirr):
            #print (dirr+'/'+dongxi)
            if os.path.isdir(dirr+'/'+dongxi):
                print ('Directory:'+dirr+'/'+dongxi)
                mywalker(dirr+'/'+dongxi)
            elif os.path.isfile(dirr+'/'+dongxi):
                print ('File:'+dirr+'/'+dongxi)
    else:
        print ('Not a Directory!')


mywalker(input('Enter a Directory...\n'))
