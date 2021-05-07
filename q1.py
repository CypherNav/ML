from threading import Thread
import time
var=2
terminate=False
change=False
def printVar():
    global var
    global terminate
    global change
    i=1
    while True:
        if change:
            i=1
            change=False
        print(var,"X",i,"=",var*i)
        i=i+1
        time.sleep(1)
        if terminate:
            return
def changeVar():
    global var
    global terminate
    global change
    try:
        while True:
            var=int(input())
            change=True
    except ValueError:
        terminate=True
        return
thr1=Thread(target=printVar)
thr2=Thread(target=changeVar)
thr1.start()
thr2.start()
