import threading
import time
time1=time.time()
lock=threading.Lock()
var=0
def thread_1():
    for i in range(500000):
        global var
        lock.acquire()
        var = var + 1
        lock.release()

def thread_2():
    for i in range(500000):
        global var
        lock.acquire()
        var = var - 1
        lock.release()


t1 = threading.Thread(target=thread_1, args=(), name='Thread_1')
t2 = threading.Thread(target=thread_2, args=(), name='Thread_2') 

t1.start()
t2.start()
t1.join()
t2.join()
print(var)
time2=time.time()
time=time2-time1
print(time)
