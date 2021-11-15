import time
import threading
time1=time.time()
var = 0

def add():
    global var
    for i in range(5000000):
        var = var + 1        
def minus():
    global var
    for i in range(5000000):
        var = var - 1

#for i in range(5000000):
#    add()
#    minus()
thread1 = threading.Thread(target=add()) 
thread1.start()
thread2 = threading.Thread(target=minus()) 
thread2.start()
thread1.join()
thread2.join()
time2=time.time()
time=time2-time1
print(var)
print(time)