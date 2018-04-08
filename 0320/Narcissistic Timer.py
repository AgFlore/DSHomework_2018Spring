import time;
class myTimer():
    def __init__(self):
        self.starttime=0
        self.stoptime=0
        self.started = False
        self.stopped = False

    def start(self):
        self.starttime = time.time()
        self.started = True

    def stop(self):
        self.stoptime = time.time()
        self.stopped = True

    def __str__(self):
        if self.stopped:
            output = 'It took '+str(self.stoptime-self.starttime)+' second(s).'
            return output
        else:
            if self.started:
                return ('Timer not stopped...')
            else:
                return ('Timer not started...')

def Narciss (n):
    outlist = []
    for i in range(10**(n-1),10**(n)):
        j = list(str(i))
        s = 0
        for k in j:
            s+=int(k)**n
        if s == i:
            outlist.append(i)
    return (outlist)

a = myTimer()
a.start()
print(Narciss(4))
a.stop()
print(a)
